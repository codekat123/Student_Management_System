from .create import ProfessorCreateAPIView
from .delete import ProfessorDestroyAPIView
from .list import ProfessorListAPIView
from .update import (
     ProfessorUpdateOnlyProfessor,
     ProfessorUpdateOnlyAdmin,
)

from .detail import (
     ProfessorDetailOnlyProfessor,
     ProfessorDetailOnlyAdmin
)