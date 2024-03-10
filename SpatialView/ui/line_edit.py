#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets

from SpatialView.ui.abstract_widget_type import AbstractWidgetType
from functools import partial


class LineEdit(AbstractWidgetType):
    def render(self, target):
        value_widget = QtWidgets.QLineEdit()
        value_widget.setText(target.__getattribute__(self.property))
        value_widget.textChanged.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget
