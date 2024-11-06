import msvcrt


class Bill:
    def __init__(self, date, amount, category, note, is_income=True):
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note
        self.is_income = is_income

    def __str__(self):
        if self.is_income:
            return f"收入: {self.date} - 金额: {self.amount} - 类别: {self.category} - 备注: {self.note}"
        else:
            return f"支出: {self.date} - 金额: {self.amount} - 类别: {self.category} - 备注: {self.note}"


class BudgetManager:
    def __init__(self):
        self.income_bills = []
        self.expense_bills = []

    def add_income(self, date, amount, category, note):
        if amount <= 0:
            print("收入金额必须为正数")
            return
        self.income_bills.append(Bill(date, amount, category, note, True))

    def add_expense(self, date, amount, category, note):
        if amount <= 0:
            print("支出金额必须为正数")
            return
        self.expense_bills.append(Bill(date, amount, category, note, False))

    def display_all(self):
        print("收入记录:")
        for bill in self.income_bills:
            print(bill)
        print("\n支出记录:")
        for bill in self.expense_bills:
            print(bill)

    def query_by_date(self, date):
        # 假设这里只按完整日期查询
        def match_date(bill):
            return bill.date == date

        income_matches = [bill for bill in self.income_bills if match_date(bill)]
        expense_matches = [bill for bill in self.expense_bills if match_date(bill)]

        if income_matches:
            print(f"日期 {date} 的收入记录:")
            for bill in income_matches:
                print(bill)

        if expense_matches:
            print(f"日期 {date} 的支出记录:")
            for bill in expense_matches:
                print(bill)

    def main_menu(self):
        while True:
            print("============================")
            print("   欢迎使用个人账单管理系统")
            print("============================")
            print("请选择操作:")
            print("1. 记录收入")
            print("2. 记录支出")
            print("3. 查看所有账单")
            print("4. 按日期查询账单")
            print("5. 退出系统")
            choice = input("请输入选择序号(1-5): ")

            if choice == '1':
                print("============================")
                print("   欢迎使用个人账单管理系统")
                print("============================")
                print("请输入收入信息:")
                date = input("输入日期(YYYY-MM-DD): ")
                amount = float(input("输入金额: "))
                category = input("输入类别: ")
                note = input("输入备注(可选): ")
                self.add_income(date, amount, category, note)
                print("收入已成功记录！")
                esc=input("按回车键返回主菜单...")
            elif choice == '2':
                print("============================")
                print("   欢迎使用个人账单管理系统")
                print("============================")
                print("请输入支出信息:")
                date = input("输入日期(YYYY-MM-DD): ")
                amount = float(input("输入金额: "))
                category = input("输入类别: ")
                note = input("输入备注(可选): ")
                self.add_expense(date, amount, category, note)
                print("支出已成功记录！")
                esc = input("按回车键返回主菜单...")
            elif choice == '3':
                self.display_all()
                esc = input("按回车键返回主菜单...")
            elif choice == '4':
                date = input("输入查询日期(YYYY-MM-DD): ")
                self.query_by_date(date)
                esc = input("按回车键返回主菜单...")
            elif choice == '5':
                print("感谢使用，再见！")
                break
            else:
                print("无效输入，请重新选择。")

            # 使用示例


if __name__ == "__main__":
    manager = BudgetManager()
    manager.main_menu()