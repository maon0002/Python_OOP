from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("TestGuy1")
        self.student_with_course = Student(
            "TestGuy2"
            , {"math": ["some note"]}
        )

    def test_correct_initialization(self):
        self.assertEqual("TestGuy1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual(
            {"math": ["some note"]},
            self.student_with_course.courses
        )

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.enroll(
            "math",
            ["second note"]
        )

        self.assertEqual(
            "second note",
            self.student_with_course.courses["math"][1]
        )

        self.assertEqual(
            "Course already added. Notes have been updated.",
            result
        )

    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student.enroll(
            "math",
            ["math notes"]
        )

        self.assertEqual(
            "math notes",
            self.student.courses["math"][0]
        )

        self.assertEqual(
            "Course and course notes have been added.",
            result
        )

    def test_add_notes_to_non_existing_course_with_third_param(self):
        result = self.student.enroll(
            "math",
            ["math notes"],
            "Y"
        )

        self.assertEqual(
            "math notes",
            self.student.courses["math"][0]
        )

        self.assertEqual(
            "Course and course notes have been added.",
            result
        )

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll(
            "math",
            ["math notes"],
            "N"
        )

        self.assertEqual(
            0,
            len(self.student.courses["math"])
        )

        self.assertEqual(
            "Course has been added.",
            result
        )

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes(
            "math",
            "new note"
        )

        self.assertEqual(
            "new note",
            self.student_with_course.courses["math"][-1]
        )

        self.assertEqual(
            "Notes have been updated",
            result
        )

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "some note")

        self.assertEqual(
            "Cannot add notes. Course not found.",
            str(ex.exception)
        )

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")

        self.assertEqual(
            {},
            self.student_with_course.courses
        )

        self.assertEqual(
            "Course has been removed",
            result
        )

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual(
            "Cannot remove course. Course not found.",
            str(ex.exception)
        )


if __name__ == "__main__":
    main()