from .students import (
     StudentCreateAPIView,
     StudentDestroyAPIView,
     StudentListAPIView,
     StudentUpdateOnlyStudent,
     StudentUpdateOnlyAdmin,
     StudentDetailOnlyStudent,
     StudentDetailOnlyAdmin,
)
from .professors import (
     ProfessorCreateAPIView,
     ProfessorDestroyAPIView,
     ProfessorListAPIView,
     ProfessorUpdateOnlyProfessor,
     ProfessorUpdateOnlyAdmin,
     ProfessorDetailOnlyProfessor,
     ProfessorDetailOnlyAdmin,
)