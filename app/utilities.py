
class Winner:
    def determine_winner(self, move1, move2):
        winning_combinations = {
            "Piedra": "Tijera",
            "Tijera": "Papel",
            "Papel": "Piedra"
        }
        
        if move1 == move2:
            return "Empate"
        elif winning_combinations[move1] == move2:
            return "Jugador 1"
        else:
            return "Jugador 2"
        
    def get_winners(self, round_results, p1, p2):
        winners = []
        for round in round_results:
            winner_name = p1.name if round.winner == "Jugador 1" else p2.name if round.winner == "Jugador 2" else "Empate"
            winners.append({
                "round_number": round.round_number,
                "winner_name": winner_name
            })
        return winners
            