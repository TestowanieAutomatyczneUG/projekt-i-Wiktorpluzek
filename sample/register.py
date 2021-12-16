import unittest


class Register:
    def __init__(self, students):
        self.students = students
        self.subjects = ["maths", "physics", "english", "biology", "geography", "arts"]

    def check_id(self, passedId):
        if type(passedId) is not int:
            if type(passedId) in [float, str]:
                passedId = int(float(str(passedId)))
                return passedId
            else:
                raise ValueError("Id must be an integer")
        return passedId

    def get_allStudents(self):
        return self.students

    def get_Student(self, studId):
        for stud in self.students:
            if stud['id'] is studId:
                return stud
        return None

    def add_Student(self, studId, studName, studSurname):
        if self.get_Student(studId) is None:
            studId = self.check_id(studId)
            if type(studName) is not str:
                raise TypeError("Student name must be a string")
            if type(studSurname) is not str:
                raise TypeError("Student surname must be a string")
            self.students.append({"id": studId, "name": studName, "surname": studSurname, "subjects": []})
            return self.get_Student(studId)
        else:
            raise Exception("Student ID already taken. Perhaps the student is already in the register?")

    def edit_Student(self, studId, updateId=None, updateName=None, updateSurname=None):
        studId = self.check_id(studId)
        if type(updateName) is not str:
            raise TypeError("Student name must be a string")
        if type(updateSurname) is not str:
            raise TypeError("Student surname must be a string")
        if type(updateId) is not int and updateId is not None:
            if type(updateId) in [float, str]:
                updateId = int(float(str(updateId)))
            else:
                raise ValueError("Updated Id must be an integer")
        for stud in self.students:
            if stud['id'] is studId:
                if updateId is not None:
                    stud['id'] = updateId
                if updateName is not None:
                    stud['name'] = updateName
                if updateSurname is not None:
                    stud['surname'] = updateSurname
                return stud
        raise Exception("Student with such id does not exist")

    def remove_Student(self, studId):
        studId = self.check_id(studId)
        i=0
        for stud in self.students:
            if stud['id'] is studId:
                tmp = self.students[i]
                del self.students[i]
                return tmp
            i += 1
        raise Exception("Student with such id does not exist")

    def add_subject(self, studId, subject):
        studId = self.check_id(studId)
        if subject not in self.subjects:
            raise Exception("No such subject is taught right now")
        else:
            for stud in self.students:
                if stud['id'] is studId:
                    stud['subjects'].append({
                        "subject": subject,
                        "notes": []
                    })
                    return stud

    def edit_subject(self, studId, subject, updsubject):
        studId = self.check_id(studId)
        if subject not in self.subjects or updsubject not in self.subjects:
            raise Exception("No such subject is taught right now")
        for stud in self.students:
            if stud['id'] is studId:
                for subj in stud['subjects']:
                    if subj["subject"] is subject:
                        subj["subject"] = updsubject
                    return stud
                return Exception("This student does not attend this subject")

    def remove_subject(self, studId, subject):
        studId = self.check_id(studId)
        exists=False
        for stud in self.students:
            if stud['id'] is studId:
                exists=True
        if not exists:
            raise Exception("Student with this id does not exist")
        for stud in self.students:
            if stud['id'] is studId:
                i=0
                for subj in stud['subjects']:
                    if subj["subject"] is subject:
                        del stud['subjects'][i]
                        return stud
                    i+=1
                raise Exception("This student doest not study such subject")

    def check_notes(self, notes):
        i=0
        for note in notes:
            if type(note) not in [float, int]:
                raise ValueError("Note must be a float or int")
            if type(note) is float:
                note = round(note, 2)
                notes[i]=note
            i+=1
        return notes

    def add_notes(self, studId, subject, notes):
        if type(notes) not in [int, float, list]:
            raise ValueError("Notes must be float, int or list")
        if type(notes) is list:
            notes = self.check_notes(notes)
        studId = self.check_id(studId)
        for stud in self.students:
            if stud['id'] is studId:
                for subj in stud['subjects']:
                    if subj['subject'] is subject:
                        if type(notes) is int:
                            subj['notes'].append(notes)
                        if type(notes) is list:
                            for note in notes:
                                subj['notes'].append(note)
                        return stud
                raise Exception("This student does not study such subject")

    def edit_notes(self, studId, subject, notes):
        studId = self.check_id(studId)
        if type(notes) not in [int, float, list]:
            raise ValueError("Notes must be float, int or list")
        if type(notes) is list:
            notes = self.check_notes(notes)
        for stud in self.students:
            if stud['id'] is studId:
                for subj in stud['subjects']:
                    if subj['subject'] is subject:
                        if type(notes) is list:
                            subj['notes'] = notes
                        if type(notes) is int:
                            subj['notes'] = list(notes)
                        return stud






