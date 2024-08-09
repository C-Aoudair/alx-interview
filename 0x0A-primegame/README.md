# Prime Game

This module determines the winner of a game played between two players, Maria and Ben. The game involves picking prime numbers from a set of numbers, and the player who cannot pick a prime number loses the round.

## Function

### `isWinner(x, nums)`

This function calculates the winner after `x` rounds of the game.

#### Parameters:

- `x` (int): The number of rounds to be played.
- `nums` (list of int): A list where each element represents the maximum number considered in each round.

#### Returns:

- `str`: `"Maria"` if Maria wins the most rounds.
- `str`: `"Ben"` if Ben wins the most rounds.
- `None`: If there is a tie.

### Example Usage:

```python
x = 3
nums = [4, 5, 1]

winner = isWinner(x, nums)
print(winner)  # Output: "Maria", "Ben", or None based on the game result

