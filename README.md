# PyTeal assignment

In this assignment, you will be tasked to complete the PyTeal stateless program in `pyteal_program.py` that checks the atomic transfer performed in `scripts/main.js`.

The transactions performed is in `scripts/main.js` consists of an asset create transaction, followed by an atomic transfer consisting of 

1. Asset opt in transaction
2. Asset transfer transaction
3. Payment transaction of 5 Algos to the asset creator

If the checks passes, the contract will be able to sign the transactions on behalf of the asset receiver account and submit them.

Perform the following checks in the program,

1. No. of transactions in the group
2. Correct asset ID
3. Correct receiver address
4. Correct amount of Algos in the payment
5. Correct creator address

## Setup instructions

### Install python packages via AlgoKit
run `algokit bootstrap poetry` within this folder

### Install JS packages
run `yarn install`

### Update environement variables
1. Copy `.env.example` to `.env`
2. Update Algorand Sandbox credentials in `.env` file
3. Update accounts in `.env` file

### Initialize virtual environment
run `poetry shell`

### Compile contracts
run `python pyteal_program.py`

### Submit transaction
run `node scripts/main.js`