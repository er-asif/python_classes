#attendance management using set
all_students = {1001,1002,1003,1004,1005,1006,1007,1008}
present_students = set()
print("""
Press 1 to mark attendance
Press 2 to view attendance
Press 3 to exit..
""")

while True:
	ch = int(input("Enter choice -> "))
	if ch==1:
		rollno = int(input("Enter Roll No"))
		if rollno in all_students:
			present_students.add(rollno)
			print(f"Attendance marked for {rollno}")
		else:
			print("This rollno is not registered")
	elif ch==2:
		print("Today's Present = ",present_students)
		print("Today's Absent = ",all_students - present_students)
	elif ch==3:
		break
	else:
		print("Invalid Choice")