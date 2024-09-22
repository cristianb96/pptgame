from .models import Player, GameRound
from .config import db

class InGame:
    
    @staticmethod
    def get_by_name(nm):
        return Player.query.filter_by(name=nm).first()
    
    @staticmethod
    def add_player(nm_player):
        player = Player(name=nm_player)
        db.session.add(player)
        db.session.commit()
        
    @staticmethod
    def get_player(player):
        return Player.query.get(player)

    @staticmethod
    def get_round_results(game_id):
        return GameRound.query.filter_by(game_id=game_id).all()
    
    @staticmethod
    def increment_round(game):
        game.round_number += 1
        #db.session.commit()
    
    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def update_game(game, move1=None, move2=None):
        if move1:
            game.player1_move = move1
            game.current_turn = 'player2'
        if move2:
            game.player2_move = move2
            game.current_turn = 'player1'
        db.session.commit()
    
    @staticmethod
    def add_round_result(game_id, winner, round_number):
        round_result = GameRound(game_id=game_id, winner=winner, round_number=round_number)
        db.session.add(round_result)
        
    def clear_round_results(game_id):
        GameRound.query.filter_by(game_id=game_id).delete()
