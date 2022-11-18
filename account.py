class Account:

    def __init__(self, name: str) -> None:
        """
        This function initializes an account with balance of 0.

        :param name: This is the account name
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This function takes an amount to deposit into the associated class account and adds that total to the
        account_balance as long as that amount is greater than 0 and then return 'True' if the transaction was
        successful and 'False' if the transaction failed
        :param amount: This is the amount to be deposited into account_balance
        :return: Returns 'True' for successful deposit and 'False' for a failed deposit
        """

        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True

        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This function takes an amount to withdraw from the associated class account and subtracts that total
        from the account_balance as long as that amount is greater than 0 and less than the account_balance
        total and then returns 'True' if the transaction was successful and 'False' if the transaction failed
        :param amount: This is the amount to be withdrawn from account_balance
        :return: Returns 'True' for successful withdrawal and 'False' for a failed withdrawal
        """

        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance = self.__account_balance - amount
            return True

        else:
            return False

    def get_balance(self) -> float:
        """
        This function returns the current account_balance value
        :return: Returns the value of 'account_balance'
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        This function returns the account_name value
        :return: Returns the name of 'account_name'
        """
        return self.__account_name




