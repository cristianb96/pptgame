from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .config import db

Base = declarative_base()

class Player(db.Model):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    

class GameRound(db.Model):
    __tablename__ = 'game_rounds'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    winner = Column(String)
    round_number = Column(Integer, default=1)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game")#, back_populates="rounds_game"


class Game(db.Model):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    player1_move = Column(String, nullable=False)
    player2_move = Column(String, nullable=False)
    current_turn = Column(String, nullable=False)
    winner_count_player1 = Column(Integer, default=0)
    winner_count_player2 = Column(Integer, default=0)
    round_number = Column(Integer, default=1)
    #rounds_game = relationship("GameRound", back_populates="game")