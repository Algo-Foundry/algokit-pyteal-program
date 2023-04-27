from pyteal import *

ASSET_CREATOR = Addr("FA3CFQSFJIBPLSOM37SCQR5666DALRAORRSI5LAFDA2SICSZZ3MU6A7ALE")
ASSET_SENDER = Addr("LHRYGXNIMZKE24FXS3A5DCTPHCA63H6HYIGITBKEQJB4JPZ3FIQ6SYUNS4")


def pyteal_program():
    return Seq(
        Assert(Global.group_size() == Int(3)),
        # Asset opt in
        Assert(Gtxn[0].type_enum() == TxnType.AssetTransfer),
        Assert(Gtxn[0].asset_amount() == Int(0)),
        Assert(Gtxn[0].sender() == ASSET_SENDER),
        Assert(Gtxn[0].asset_receiver() == ASSET_SENDER),
        # Payment of 5 Algos
        Assert(Gtxn[1].type_enum() == TxnType.Payment),
        Assert(Gtxn[1].amount() == Int(5_000_000)),
        Assert(Gtxn[1].sender() == ASSET_SENDER),
        Assert(Gtxn[1].receiver() == ASSET_CREATOR),
        # Asset transfer
        Assert(Gtxn[2].type_enum() == TxnType.AssetTransfer),
        Assert(Gtxn[2].asset_amount() == Int(1)),
        Assert(Gtxn[2].sender() == ASSET_CREATOR),
        Assert(Gtxn[2].asset_receiver() == ASSET_SENDER),
        # Approve if all assertions pass
        Approve(),
    )


if __name__ == "__main__":
    stateless_sc = compileTeal(pyteal_program(), mode=Mode.Signature, version=8)
    with open("./artifacts/pyteal_program.teal", "w") as f:
        f.write(stateless_sc)
