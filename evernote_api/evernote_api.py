import EvernoteClient, NoteStore

dev_token = "put your dev token here"
client = EvernoteClient(token=dev_token)


def auth_user():
    userStore = client.get_user_store()
    user = userStore.getUser()
    return user.username


def get_notes(search_term, filter_type):
    filter = NoteStore.NoteFilter()
    if filter_type == "words":
        filter.words = search_term
    elif filter_type == "guid":
        filter.notebookGuid = search_term
    if filter_type == "tags":
        filter.tagGuids = [term for term in search_term]

    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True

    ourNoteList = noteStore.findNotesMetadata(authToken, filter, 0, 100, spec)

    wholeNotes = []
    for note in ourNoteList.notes:
        wholeNote = noteStore.getNote(authToken, note.guid, True)
        print
        "Content length: %d" % wholeNote.contentLength
        wholeNotes.append(wholeNote)