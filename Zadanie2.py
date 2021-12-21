import unittest
from unittest.mock import MagicMock, patch

class Note:
    def __init__(self, name, note):
        if name is None:
            raise Exception("Name can't be null")
        elif type(name) is not str:
            raise Exception("Name must be str")
        elif len(name)==0:
            raise Exception("Length of name can't be 0")
        elif type(note) is not float:
            raise Exception("Note must be float")
        elif not 2<= note <=6:
            raise Exception("Note must be between 2 and 6")
        self.name = name
        self.note = note

    def getName(self):
        return self.name
    
    def getNote(self):
        return self.note

class NoteStorage:
    def add(self, note):
        pass

    def clear(self):
        pass

    def getAllNotesOf(self, name):
        pass

class NoteService:
    def __init__(self):
        self.noteStorage = NoteStorage()

    def add(self, note):
        return self.noteStorage.add(note)

    def averageOf(self, name):
        allNotes = self.noteStorage.getAllNotesOf(name)
        noteSum = 0
        for note in allNotes:
            noteSum+=note.note
        numOfNotes = len(allNotes)
        if numOfNotes == 0:
            return 0
        return noteSum / numOfNotes

    def clear(self):
        return self.noteStorage.clear()

class NoteServiceTest(unittest.TestCase):    
    def test_note_service_add_note(self):
        noteService = NoteService()
        note = Note("note", 3.21)
        with patch.object(NoteStorage, 'add', MagicMock(return_value=True)):
            self.assertEqual(noteService.add(note), True)
        
    def test_averageOf_many_notes(self):
        noteService = NoteService()
        allNotes = [Note("note", 3.0), Note("note", 5.0), Note("note", 2.0), Note("note", 2.0)]
        with patch.object(NoteStorage, 'getAllNotesOf', MagicMock(return_value=allNotes)):
            self.assertAlmostEqual(noteService.averageOf("note"), 3.0)

    def test_averageOf_one_note(self):
        noteService = NoteService()
        allNotes = [Note("note", 3.0)]
        with patch.object(NoteStorage, 'getAllNotesOf', MagicMock(return_value=allNotes)):
            self.assertEqual(noteService.averageOf("note"), 3.0)
        
    def test_averageOf_no_notes(self):
        noteService = NoteService()
        allNotes = []
        with patch.object(NoteStorage, 'getAllNotesOf', MagicMock(return_value=allNotes)):
            self.assertEqual(noteService.averageOf("note"), 0.0)
        
    def test_clear(self):
        noteService = NoteService()
        with patch.object(NoteStorage, 'clear', MagicMock(return_value=None)):
            self.assertIsNone(noteService.clear())
