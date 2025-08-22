# app.py
import os
import sys

from flask import Flask, Response, redirect, render_template, url_for

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.my_minesweeper.minesweeper import Minesweeper

app = Flask(__name__)

# Create a new game
game = Minesweeper(5, 5, 3)


@app.route("/")
def index() -> str:
    board = game.get_board()
    if game.is_winner():
        return render_template("index.html", board=board, message="🔥 You Win! 🔥")
    return render_template("index.html", board=board)


@app.route("/reveal/<int:row>/<int:col>")
def reveal(row: int, col: int) -> Response:
    result = game.reveal(row, col)
    if result == "Game Over":
        return render_template("index.html", board=game.board, message="🥲 Game Over! 🥲")
    return redirect(url_for("index"))


@app.route("/restart")
def restart() -> Response:
    game.restart()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
