from collections import Counter


class Hand:
    def __init__(self, line: str, order: list[str] = list("AKQJT98765432"), q: int = 1):
        self.hand, self.bid = line.split(" ")
        self.type_1: int = self.get_t1()
        self.type_2: int = self.get_t2() if q == 2 else self.type_1
        self.order = order if q == 1 else list("AKQT98765432J")

    def get_t1(self):
        ll = list(Counter(self.hand).values())
        return (
            max(ll) + 2 if max(ll) >= 4 else max(ll) + min(ll) if max(ll) == 3 else ll.count(2) + 1
        )

    def get_t2(self):
        jj = Counter(self.hand)["J"]
        return (
            self.type_1 if not jj else 7 if self.type_1 in [5, 6, 7] else 6 if self.type_1 == 4
            else self.type_1 + jj + 1 if self.type_1 == 3 else self.type_1 * 2
        )

    def __gt__(self, new):
        if self.type_2 == new.type_2:
            for idx in range(len(self.hand)):
                if new.hand[idx] == self.hand[idx]:
                    continue
                else:
                    return self.order.index(new.hand[idx]) < self.order.index(self.hand[idx])
        return new.type_2 > self.type_2


f_in = open("input7", "r").read().splitlines()

hl_q1: list[Hand] = [Hand(line) for line in f_in]
print(f"Question 1: {sum([int(o.bid) * (len(hl_q1) - i) for i, o in enumerate(sorted(hl_q1))])}")

hl_q2: list[Hand] = [Hand(line, q=2) for line in f_in]
print(f"Question 2: {sum([int(o.bid) * (len(hl_q2) - i) for i, o in enumerate(sorted(hl_q2))])}")
