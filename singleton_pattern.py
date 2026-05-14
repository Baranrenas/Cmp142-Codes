class school:
    __instance = None

    def __new__(cls, name, course, nationality):

        # Create object only once
        if cls.__instance is None:

            cls.__instance = super(school, cls).__new__(cls)

            cls.__instance.name = name
            cls.__instance.course = course
            cls.__instance.nationality = nationality

        return cls.__instance


# First student
ali = school('kyrenia university student', 'cmp142', 'turkey')
print(ali.name, ali.course, ali.nationality)

# Second student
mehmet = school('near east student', 'cmp241', 'turkey')
print(mehmet.name, mehmet.course, mehmet.nationality)

# Third student
daniel = school('daniel university', 'cmp144', 'nigeria')
print(daniel.name, daniel.course, daniel.nationality)