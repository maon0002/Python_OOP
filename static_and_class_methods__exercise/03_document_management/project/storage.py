from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):  # - add the category if it is not in the list
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):  # - add the topic if it does not exist
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):  # - add the document if it does not exist
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):  # - edit the name of the category with the provided id
        category = [c for c in self.categories if c.id == category_id][0]
        Category.edit(category, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):  # - edit the topic with the given id
        topic = [t for t in self.topics if t.id == topic_id][0]
        Topic.edit(topic, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):  # - edit the document with the given id
        doc = self.get_document(document_id)
        Document.edit(doc, new_file_name)

    def delete_category(self, category_id):  # - delete the category with the provided id
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):  # - delete the topic with the provided id
        topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):  # - delete the document with the provided id
        doc = self.get_document(document_id)
        self.documents.remove(doc)

    def get_document(self, document_id):  # - return the document with the provided id
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):  # - returns a string representation of each document on separate lines
        return "\n".join([
            str(d) for d in self.documents
        ])
