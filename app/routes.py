from flask import Flask, render_template, request, jsonify, redirect, url_for
from .exceptions import GameException
from .selects import InGame
from .config import db, Database
import os
from .utilities import Winner
from .models import Game, GameRound, Player


def register_routes(app):
    @app.route('/', methods=['GET'])
    def redirect_to():
        return redirect(url_for("register"))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            try:
                player1 = request.form.get('p1')
                player2 = request.form.get('p2')

                if not player1 or not player2:
                    raise GameException('Los jugadores deben ser ingresados')
                
                if player1 == player2:
                    raise GameException('Los nombres son iguales')
                
                if InGame.get_by_name(player1) or InGame.get_by_name(player2):
                    raise GameException('Uno de los jugadores ya existe')
                
                InGame.add_player(player1)
                InGame.add_player(player2)
                
                new_game = Game(
                    player1_id=InGame.get_by_name(player1).id, 
                    player2_id=InGame.get_by_name(player2).id, 
                    current_turn='player1', 
                    player1_move="", 
                    player2_move="",
                    round_number=1
                )
                db.session.add(new_game)
                db.session.commit()
                
                return jsonify({"success": True, "game_id": new_game.id}), 201

            except GameException as e:
                return jsonify(e.to_dict()), 400
            
            except Exception as e:
                print(e)
                return jsonify({"error": "Lo siento, no es posible registrarse. Intente mas tarde."}), 500
        return render_template('register.html')


    @app.route('/play', methods=['GET', 'POST'])
    def play():
        game_id = request.args.get('game_id')
        game = Game.query.get(game_id)

        if not game:
            return jsonify({"error": "Juego no encontrado"}), 404

        if request.method == 'POST':
            move1 = request.form.get('move1')
            move2 = request.form.get('move2')

            if game.current_turn == 'player1':
                
                InGame.update_game(game, move1=move1)

                player1 = InGame.get_player(game.player1_id)
                player2 = InGame.get_player(game.player2_id)

                return render_template(
                    'game.html', 
                    player1=player1, 
                    player2=player2, 
                    current_turn=game.current_turn, 
                    game=game, 
                    n_r=game.round_number, 
                    next_round=False
                )

            elif game.current_turn == 'player2':
                
                InGame.update_game(game, move2=move2)

                p1 = InGame.get_player(game.player1_id)
                p2 = InGame.get_player(game.player2_id)

                result = Winner().determine_winner(game.player1_move, game.player2_move)
                
                if result == "Jugador 1":
                    game.winner_count_player1 += 1
                elif result == "Jugador 2":
                    game.winner_count_player2 += 1
                
                InGame.add_round_result(game_id, result, game.round_number)
                
                round_results = InGame.get_round_results(game_id)
                winners = Winner().get_winners(round_results, p1, p2)
                
                if game.winner_count_player1 == 3 or game.winner_count_player2 == 3:
                    winner_name = p1.name if game.winner_count_player1 == 3 else p2.name
                    InGame.commit()

                    return render_template(
                        'game.html',
                        player1=p1, 
                        player2=p2, 
                        current_turn=game.current_turn, 
                        game=game, 
                        n_r=game.round_number, 
                        round_results=winners,
                        next_round=False,
                        game_over=True,
                        player_win=winner_name
                    )
                    
                InGame.increment_round(game)
                InGame.commit()

                return render_template(
                    'game.html', 
                    player1=p1, 
                    player2=p2, 
                    current_turn=game.current_turn, 
                    game=game, 
                    n_r=game.round_number, 
                    round_results=winners,
                    next_round=True
                )

        player1 = InGame.get_player(game.player1_id)
        player2 = InGame.get_player(game.player2_id)

        return render_template(
            'game.html', 
            player1=player1, 
            player2=player2, 
            current_turn=game.current_turn, 
            game=game, 
            n_r=game.round_number,
            next_round=False
        )


    @app.route('/reset/<game_id>', methods=['POST'])
    def reset(game_id):
        game = Game.query.get(game_id)
        if not game:
            return jsonify({"error": "Juego no encontrado."}), 404
        
        game.winner_count_player1 = 0
        game.winner_count_player2 = 0
        game.round_number = 1
        game.current_turn = 'player1'
        
        InGame.clear_round_results(game_id)
        InGame.commit()

        return redirect(url_for('play', game_id=game_id))
