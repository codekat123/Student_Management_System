from .create import StudentCreateAPIView
from .delete import StudentDestroyAPIView
from .list import StudentListAPIView
from .update import (
     StudentUpdateOnlyStudent,
     StudentUpdateOnlyAdmin,
)

from .detail import (
     StudentDetailOnlyStudent,
     StudentDetailOnlyAdmin
)