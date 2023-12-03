from unittest import TestCase


class GameRound:
    def __init__(self, line: str):
        self.red, self.green, self.blue = self._get_colours(line)

    def __str__(self):
        return f"{self.red=} {self.green=} {self.blue=}"

    @staticmethod
    def _get_colours(line: str) -> tuple[int, int, int]:
        colour_entries = line.split(",")
        # print(colour_entries)
        colour_values = {}
        for entry in colour_entries:
            value, colour = entry.lstrip(" ").rstrip("\n").split(" ")
            colour_values[colour] = int(value)
        return colour_values.get("red", 0), colour_values.get("green", 0), colour_values.get("blue", 0)

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        return all([self.red <= red, self.green <= green, self.blue <= blue])


class Game:
    def __init__(self, line: str):
        self.id = self._get_id(line)
        self.rounds = self._get_rounds(line)

    @staticmethod
    def _get_id(line: str) -> int:
        return int(line.split(":")[0].split(" ")[1])

    @staticmethod
    def _get_rounds(line: str) -> list[GameRound]:
        records = line.split(":")[1].split(";")
        rounds = []
        for record in records:
            rounds.append(GameRound(record))
        return rounds

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        # print(red, green, blue)
        # [print(game_round) for game_round in self.rounds]
        return all(map(lambda game_round: game_round.is_possible(red, green, blue), self.rounds))


class Day2Part1:
    def __init__(self):
        self.sample_input = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
        self.cubes = {
            "red": 12,
            "green": 13,
            "blue": 14
        }

    def sum_possible_ids(self, data: list[str]) -> int:
        possible_game_ids = []
        for entry in data:
            game = Game(entry)
            if game.is_possible(red=self.cubes["red"], green=self.cubes["green"], blue=self.cubes["blue"]):
                possible_game_ids.append(game.id)
                # print(entry, end="")
        return sum(possible_game_ids)

    def demo(self):
        print("Game.parse_data")
        possible_game_ids = []
        for entry in self.sample_input:
            game = Game(entry)
            print(f"\t{entry}\n\t\t-> {game.id=}")
            [print(f"\t\t-> {game_round}") for game_round in game.rounds]
            if game.is_possible(red=self.cubes["red"], green=self.cubes["green"], blue=self.cubes["blue"]):
                possible_game_ids.append(game.id)
        print(f"{sum(possible_game_ids)=}")

    def test(self):
        TestCase().assertEqual(8, self.sum_possible_ids(self.sample_input))

    def solve(self, file_path: str) -> int:
        data = []
        with open(file_path, "r") as input_file:
            for line in input_file:
                data.append(line)
        return self.sum_possible_ids(data)


def main():
    print("Advent of Code 2023 - Day 2: Cube Conundrum")

    part1 = Day2Part1()
    # part1.demo()
    part1.test()
    print(part1.solve("input.txt"))


if __name__ == "__main__":
    main()
