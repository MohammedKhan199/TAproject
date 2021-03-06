from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from Classes.functions import *

class SectionTestCase(TestCase):

    def setUp(self):
        self.course1 = Course.objects.create(courseid="337", name="Systems Programming",credits="3")
        self.lab1 = Section.objects.create(course=self.course1, sectionid="902", type="Lab", schedule="R @ 11:00 - 12:50")

#   CREATE COURSE TESTS
    def test_SectionIdexists(self):
        self.assertEqual(createSection(self.course1, "902", "Lab", "T @ 11:00 - 12:50"),
                         "Section with that ID already exists")

    def test_SectionCreated(self):
        createSection(self.course1, "901", "Lab", "T @ 11:00 - 12:50")
        b =Section.objects.get(sectionid="901")
        self.assertEqual("Lab", b.type)
        self.assertEqual("T @ 11:00 - 12:50", b.schedule)

    def test_noSectionid(self):
        self.assertEqual(createSection(self.course1, "", "Lab", "R @ 11:00 - 12:50"),
                         "Please fill out all required entries")

    def test_noSectionType(self):
        self.assertEqual(createSection(self.course1, "901", "", "R @ 11:00 - 12:50"), "Please fill out all required entries")

    def test_noSectionschedule(self):
        self.assertEqual(createSection(self.course1, "901", "Lab", ""), "Please fill out all required entries")


#   DELETE LAB TESTS
    def test_deletenosectionidentered(self):
        self.assertEqual(deleteSection(""), "Please enter a section ID")

    def test_deletenosectionexists(self):
        self.assertEqual(deleteSection("901"), "Section with that ID does not exist")

    def test_deletesection(self):
        self.assertEqual(self.lab1.sectionid, "902")
        self.assertEqual(deleteSection("902"), "Section with ID 902 has been deleted")
