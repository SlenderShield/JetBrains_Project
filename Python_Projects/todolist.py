from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
	__tablename__ = 'task'
	id = Column(Integer, primary_key=True)
	task = Column(String, default='default_value')
	deadline = Column(Date, default=datetime.today())

	def __repr__(self):
		return '{}. {}'.format(self.task, str(self.deadline))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
	print('Enter task ')
	task = input()
	print('Enter deadline ')
	deadline = input().split('-')
	new_row = Table(task=task,
	                deadline=datetime(int(deadline[0]), int(deadline[1]), int(deadline[2])))
	session.add(new_row)
	session.commit()
	print('The task has been added!')


def task_for_week():
	today = datetime.today()
	weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	timedelta_index = 0
	while timedelta_index < 7:
		date = today + timedelta(days=timedelta_index)
		print(f"{weekday[date.weekday()]} {date.day} {date.strftime('%b')}:")
		if not session.query(Table).filter(Table.deadline == date.date()).all():
			print('Nothing to do!\n')
		else:
			for index, value in enumerate(session.query(Table.task).filter(Table.deadline == date.date()).all()):
				print(str(index + 1) + '. ' + value[0])
			print()
		timedelta_index += 1


def task_for_today():
	today = datetime.today().date()
	print('Today {} {}'.format(today.day, today.strftime('%b')))
	if not session.query(Table).filter(Table.deadline == today).all():
		print('Nothing to do!')
	else:
		for index, value in enumerate(session.query(Table).filter(Table.deadline == today).all()):
			print(str(index + 1) + '. ' + str(value))


def all_tasks():
	lst = []
	print('All tasks: ')
	for index, task_date in enumerate(session.query(Table.task, Table.deadline).all()):
		lst.append(f"{index + 1}. {task_date[0]}. {task_date[1].day} {task_date[1].strftime('%b')}")
	for i in lst:
		print(i)


def missed_tasks():
	print('Missed tasks:')
	if not session.query(Table).filter(Table.deadline < datetime.today()).all():
		print('Nothing is missed!')
	else:
		for index, task_date in enumerate(session.query(Table.task, Table.deadline).filter(
				Table.deadline < datetime.today()).order_by(Table.deadline)):
			print(f"{index + 1}. {task_date[0]}. {task_date[1].day} {task_date[1].strftime('%b')}")


def delete_task():
	if not session.query(Table).all():
		print('Nothing to delete')
	else:
		print('Chose the number of the task you want to delete:')
		for index, task_date in enumerate(session.query(Table.task, Table.deadline).order_by(Table.deadline)):
			print(f"{index + 1}. {task_date[0]}. {task_date[1].day} {task_date[1].strftime('%b')}")
		task_number_to_delete = int(input())
		rows = session.query(Table).all()
		row_to_delete = rows[task_number_to_delete - 1]
		session.delete(row_to_delete)
		session.commit()
		print('The task has been deleted!')


def print_option():
	print('''
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit\n''')


while True:
	rows = session.query(Table).all()
	print_option()
	val = input()
	if val == '1':
		task_for_today()
	elif val == '2':
		task_for_week()
	elif val == '3':
		all_tasks()
	elif val == '5':
		add_task()
	elif val == '4':
		missed_tasks()
	elif val == '6':
		delete_task()
	else:
		print("\nBye!")
		exit()
