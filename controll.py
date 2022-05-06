import pymysql
class Human:
    def __init__(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='mysqlaqwqer2',
                             database='oop')
        self.cursor = db.cursor()

    color = "yellow"
    name = "Ivan"
    years = 5
    email = "kk@gmail.com"
#add_years
    add_years_old = ("INSERT INTO years (years_user) VALUES ('%s');")
    def add_years(self):
        write_years = int(input('Write years: '))
        old_years =(write_years)
        return old_years

#find_years_by_id
    show_years_user = ("SELECT * FROM years WHERE (id) = ('%s'); ")
    def write_id(self):
        what_id = int(input('Write id user: '))
        whats_id = what_id
        return whats_id
#add_name_for_user
    write_new_user = ("INSERT INTO name (name_user) VALUES ('%s');")
    def new_name_user(self):
        new_name = input('Write new name: ')
        namee = new_name
        return namee
#find_name
# !!!За різницю в методах return !!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    show_user_name = ("SELECT * FROM name;")
#add_color
    add_color = ("INSERT INTO color(color_user) VALUES ('%s');")
    def write_new_color(self):
        what_color = input('Input color: ')
        return what_color
#find_color
    show_color = ("SELECT * FROM color;")
#add_email
    save_email = ("INSERT INTO email(email_user) VALUES ('%s'); ")
    def write_email(self):
        how_email = input('Write Email: ')
        return how_email
#show_email
    show_email = ("SELECT * FROM email;")
    def run(self):
        while True:
            print('choise of command:\n',
                  '1.add years for user\n',
                  '2.Show years of user\n'
                  '3.Write new name\n'
                  '4.Show alls names\n'
                  '5.Add color\n'
                  '6.Show alls colors\n'
                  '7.Add email\n'
                  '8.Show emails')

            choise_command = int(input('command: '))
            if choise_command == 1:
                self.cursor.execute(self.add_years_old % self.add_years())
                print('+++ New years added')
            elif choise_command == 2:
                self.cursor.execute(self.show_years_user % self.write_id())
                print(self.cursor.fetchall())
            elif choise_command == 3:
                self.cursor.execute(self.write_new_user % self.new_name_user())
                print('+++New name added')
            elif choise_command == 4:
                self.cursor.execute(self.show_user_name)
                print(self.cursor.fetchall())
            elif choise_command == 5:
                self.cursor.execute(self.add_color % self.write_new_color())
                print('+++New color added')
            elif choise_command == 6:
                self.cursor.execute(self.show_color)
                print(self.cursor.fetchall())
            elif choise_command == 7:
                self.cursor.execute(self.save_email % self.write_email())
                print('+++New email')
            elif choise_command == 8:
                self.cursor.execute(self.show_email)
                print(self.cursor.fetchall())
