from pathlib import Path
import random

from flask import Flask, jsonify, request, send_from_directory, session

RANGE_MIN = 1
RANGE_MAX = 50
MAX_ATTEMPTS = 10

app = Flask(__name__)
app.secret_key = "change-this-key"


def reset_game():
    session["target"] = random.randint(RANGE_MIN, RANGE_MAX)
    session["attempts_left"] = MAX_ATTEMPTS
    session["guessed"] = []


@app.get("/")
def index():
    current_dir = Path(__file__).parent
    return send_from_directory(current_dir, "guess_number.html")


@app.post("/start")
def start():
    reset_game()
    return jsonify({
        "range": [RANGE_MIN, RANGE_MAX],
        "attempts_left": MAX_ATTEMPTS
    })


@app.post("/guess")
def guess():
    if "target" not in session or "attempts_left" not in session:
        reset_game()

    data = request.get_json(silent=True) or {}
    raw_guess = data.get("guess")

    attempts_left = session.get("attempts_left", MAX_ATTEMPTS)
    target = session.get("target")
    guessed = session.get("guessed", [])

    if attempts_left <= 0:
        return jsonify({
            "status": "over",
            "message": f"Better luck next time! The correct number is {target}.",
            "attempts_left": 0
        })

    try:
        guess_value = int(raw_guess)
    except (TypeError, ValueError):
        return jsonify({
            "status": "invalid",
            "message": "Invalid input. Please enter a valid number.",
            "attempts_left": attempts_left
        })

    if guess_value in guessed:
        return jsonify({
            "status": "invalid",
            "message": "You already tried that number. Pick a new one.",
            "attempts_left": attempts_left
        })

    guessed.append(guess_value)
    session["guessed"] = guessed

    attempts_left -= 1
    session["attempts_left"] = attempts_left

    if guess_value == target:
        return jsonify({
            "status": "correct",
            "message": "Congratulations! You guessed the number correctly.",
            "attempts_left": attempts_left
        })

    if attempts_left == 0:
        return jsonify({
            "status": "over",
            "message": f"Better luck next time! The correct number is {target}.",
            "attempts_left": attempts_left
        })

    if guess_value < target:
        message = "Too low! Try again."
    else:
        message = "Too high! Try again."

    return jsonify({
        "status": "continue",
        "message": message,
        "attempts_left": attempts_left
    })


if __name__ == "__main__":
    app.run(debug=True)
