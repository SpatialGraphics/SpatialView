from .vtk_mapper_data_model import VtkMapperDataModel
from .vtk_composite_data_geometry_filter_model import (
    VtkCompositeDataGeometryFilterModel,
)
from .vtk_contour_filter_model import VtkContourFilterModel
from .vtk_outline_filter_model import VtkOutlineFilterModel
from .vtk_texture_model import VtkTextureModel

import SpatialNode as sNode


def registerDataModels(ret: sNode.NodeDelegateModelRegistry):
    VtkMapperDataModel.register(ret)
    VtkTextureModel.register(ret)

    VtkCompositeDataGeometryFilterModel.register(ret)
    VtkContourFilterModel.register(ret)
    VtkOutlineFilterModel.register(ret)
