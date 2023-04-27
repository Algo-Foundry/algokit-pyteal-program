from pyteal import *


def pyteal_program():
    # Write your code here
    return Int(1)


if __name__ == "__main__":
    stateless_sc = compileTeal(pyteal_program(), mode=Mode.Signature, version=8)
    with open("./artifacts/pyteal_program.teal", "w") as f:
        f.write(stateless_sc)
