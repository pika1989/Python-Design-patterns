from abc import ABCMeta, abstractmethod


# From UML diagram it's Product
class Section(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def describe(self):
        pass


# From UML diagram these classes are ConcreteProduct
class PersonalSection(Section):
    def describe(self):
        print 'Personal Section'


class AlbumSection(Section):
    def describe(self):
        print 'Album Section'


class PatentSection(Section):
    def describe(self):
        print 'Patent Section'


class PublicationSection(Section):
    def describe(self):
        print 'Publication Section'


# From UML diagram it's Creator
class Profile(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)


# From UML diagram these classes are ConcreteCreator
class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())


if __name__ == '__main__':
    profile_type = raw_input("Which profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print "Creating profile...", type(profile).__name__
    print "Profile has sections --", profile.getSections()

