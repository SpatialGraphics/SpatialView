#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkRenderingCore import vtkActor, vtkTexture, vtkMapper

class VtkActor:
    def __init__(self):
        self._actor: vtkActor = None
    # ==========================================================================
    # =========== Blinn-Phong ==================================================
    # ==========================================================================

    # =========== Ambient ======================================================
    @property
    def ambientMax(self) -> float: ...
    @property
    def ambientMin(self) -> float: ...
    @property
    def ambient(self) -> float: ...
    @ambient.setter
    def ambient(self, value: float) -> None: ...
    @property
    def ambientColor(self) -> tuple[float, float, float]: ...
    @ambientColor.setter
    def ambientColor(self, value: tuple[float, float, float]) -> None: ...
    # =========== Diffuse ======================================================
    @property
    def diffuseMax(self) -> float: ...
    @property
    def diffuseMin(self) -> float: ...
    @property
    def diffuse(self) -> float: ...
    @diffuse.setter
    def diffuse(self, value: float) -> None: ...
    @property
    def diffuseColor(self) -> tuple[float, float, float]: ...
    @diffuseColor.setter
    def diffuseColor(self, value: tuple[float, float, float]): ...
    # =========== Specular ======================================================
    @property
    def specularMax(self) -> float: ...
    @property
    def specularMin(self) -> float: ...
    @property
    def specular(self) -> float: ...
    @specular.setter
    def specular(self, value: float) -> None: ...
    @property
    def specularColor(self) -> tuple[float, float, float]: ...
    @specularColor.setter
    def specularColor(self, value: tuple[float, float, float]) -> None: ...
    # =========== Specular Power ======================================================
    @property
    def specularPowerMax(self) -> float: ...
    @property
    def specularPowerMin(self) -> float: ...
    @property
    def specularPower(self) -> float: ...
    @specularPower.setter
    def specularPower(self, value: float) -> None: ...
    # =========== Color ======================================================

    @property
    def color(self) -> tuple[float, float, float]: ...
    @color.setter
    def color(self, value: tuple[float, float, float]) -> None: ...
    @property
    def baseColorTexture(self) -> vtkTexture: ...
    @baseColorTexture.setter
    def baseColorTexture(self, value: vtkTexture): ...
    # ============================================================================
    # =========== PBR =============================================================
    # =============================================================================

    # =========== Anisotropy ======================================================
    @property
    def anisotropyMax(self) -> float: ...
    @property
    def anisotropyMin(self) -> float: ...
    @property
    def anisotropy(self) -> float: ...
    @anisotropy.setter
    def anisotropy(self, value: float): ...
    @property
    def anisotropyRotationMax(self) -> float: ...
    @property
    def anisotropyRotationMin(self) -> float: ...
    @property
    def anisotropyRotation(self) -> float: ...
    @anisotropyRotation.setter
    def anisotropyRotation(self, value: float): ...
    @property
    def anisotropyTexture(self) -> vtkTexture: ...
    @anisotropyTexture.setter
    def anisotropyTexture(self, value: vtkTexture): ...
    # =========== IOR ======================================================
    @property
    def baseIORMax(self) -> float: ...
    @property
    def baseIORMin(self) -> float: ...
    @property
    def baseIOR(self) -> float: ...
    @baseIOR.setter
    def baseIOR(self, value: float): ...
    @property
    def coatIORMax(self) -> float: ...
    @property
    def coatIORMin(self) -> float: ...
    @property
    def coatIOR(self) -> float: ...
    @coatIOR.setter
    def coatIOR(self, value: float): ...
    # =========== Coat ======================================================
    @property
    def coatColor(self) -> tuple[float, float, float]: ...
    @coatColor.setter
    def coatColor(self, value: tuple[float, float, float]): ...
    @property
    def coatStrengthMax(self) -> float: ...
    @property
    def coatStrengthMin(self) -> float: ...
    @property
    def coatStrength(self) -> float: ...
    @coatStrength.setter
    def coatStrength(self, value: float): ...
    @property
    def coatNormalTexture(self) -> vtkTexture: ...
    @coatNormalTexture.setter
    def coatNormalTexture(self, value: vtkTexture): ...
    @property
    def coatNormalScaleMax(self) -> float: ...
    @property
    def coatNormalScaleMin(self) -> float: ...
    @property
    def coatNormalScale(self) -> float: ...
    @coatNormalScale.setter
    def coatNormalScale(self, value: float): ...
    @property
    def coatRoughnessMax(self) -> float: ...
    @property
    def coatRoughnessMin(self) -> float: ...
    @property
    def coatRoughness(self) -> float: ...
    @coatRoughness.setter
    def coatRoughness(self, value: float): ...
    # =========== Emissive ======================================================
    @property
    def emissiveFactor(self) -> float: ...
    @emissiveFactor.setter
    def emissiveFactor(self, value: float): ...
    @property
    def emissiveTexture(self) -> vtkTexture: ...
    @emissiveTexture.setter
    def emissiveTexture(self, value: vtkTexture): ...
    # =========== Normal ======================================================
    @property
    def normalScale(self) -> float: ...
    @normalScale.setter
    def normalScale(self, value: float): ...
    @property
    def normalTexture(self) -> vtkTexture: ...
    @normalTexture.setter
    def normalTexture(self, value: vtkTexture): ...
    # =========== Metallic ======================================================
    @property
    def metallicMax(self) -> float: ...
    @property
    def metallicMin(self) -> float: ...
    @property
    def metallic(self) -> float: ...
    @metallic.setter
    def metallic(self, value: float): ...
    # =========== Roughness ======================================================
    @property
    def roughnessMax(self) -> float: ...
    @property
    def roughnessMin(self) -> float: ...
    @property
    def roughness(self) -> float: ...
    @roughness.setter
    def roughness(self, value: float): ...
    # =========== OcclusionStrength ======================================================
    @property
    def occlusionStrengthMax(self) -> float: ...
    @property
    def occlusionStrengthMin(self) -> float: ...
    @property
    def occlusionStrength(self) -> float: ...
    @occlusionStrength.setter
    def occlusionStrength(self, value: float): ...
    # =========== Edge ======================================================
    @property
    def edgeTint(self) -> tuple[float, float, float]: ...
    @edgeTint.setter
    def edgeTint(self, value: tuple[float, float, float]): ...
    @property
    def edgeColor(self) -> tuple[float, float, float]: ...
    @edgeColor.setter
    def edgeColor(self, value: tuple[float, float, float]): ...
    @property
    def edgeOpacityMax(self) -> float: ...
    @property
    def edgeOpacityMin(self) -> float: ...
    @property
    def edgeOpacity(self) -> float: ...
    @edgeOpacity.setter
    def edgeOpacity(self, value: float): ...
    @property
    def edgeVisibility(self) -> int: ...
    @edgeVisibility.setter
    def edgeVisibility(self, value: int): ...
    # =========== Line ======================================================
    @property
    def lineWidthMax(self) -> float: ...
    @property
    def lineWidthMin(self) -> float: ...
    @property
    def lineWidth(self) -> float: ...
    @lineWidth.setter
    def lineWidth(self, value: float): ...
    @property
    def lineStippleRepeatFactorMax(self) -> int: ...
    @property
    def lineStippleRepeatFactorMin(self) -> int: ...
    @property
    def lineStippleRepeatFactor(self) -> int: ...
    @lineStippleRepeatFactor.setter
    def lineStippleRepeatFactor(self, value: int): ...
    @property
    def lineStipplePattern(self) -> int: ...
    @lineStipplePattern.setter
    def lineStipplePattern(self, value: int): ...
    # =========== Vertex ======================================================
    @property
    def vertexColor(self) -> tuple[float, float, float]: ...
    @vertexColor.setter
    def vertexColor(self, value: tuple[float, float, float]): ...
    @property
    def vertexVisibility(self) -> int: ...
    @vertexVisibility.setter
    def vertexVisibility(self, value: int): ...
    # =========== Point ======================================================
    @property
    def pointSizeMax(self) -> float: ...
    @property
    def pointSizeMin(self) -> float: ...
    @property
    def pointSize(self) -> float: ...
    @pointSize.setter
    def pointSize(self, value: float): ...
    # =========== ORM ======================================================
    @property
    def ORMTexture(self) -> vtkTexture: ...
    @ORMTexture.setter
    def ORMTexture(self, value: vtkTexture): ...
    # =========== Opacity ======================================================
    @property
    def opacityMax(self) -> float: ...
    @property
    def opacityMin(self) -> float: ...
    @property
    def opacity(self) -> float: ...
    @opacity.setter
    def opacity(self, value: float): ...
    # =========== Culling ======================================================
    @property
    def backFaceCulling(self) -> int: ...
    @backFaceCulling.setter
    def backFaceCulling(self, value: int): ...
    @property
    def frontFaceCulling(self) -> int: ...
    @frontFaceCulling.setter
    def frontFaceCulling(self, value: int): ...
    @property
    def showTexturesOnBackface(self) -> bool: ...
    @showTexturesOnBackface.setter
    def showTexturesOnBackface(self, value: bool): ...
    # =========== Interpolation ======================================================
    @property
    def interpolationMax(self) -> int: ...
    @property
    def interpolationMin(self) -> int: ...
    @property
    def interpolation(self) -> int: ...
    @interpolation.setter
    def interpolation(self, value: int): ...
    def interpolationString(self) -> str: ...

    # =========== Representation ======================================================
    @property
    def representationMax(self) -> int: ...
    @property
    def representationMin(self) -> int: ...
    @property
    def representation(self) -> int: ...
    @representation.setter
    def representation(self, value: int): ...
    def representationString(self) -> str: ...

    # =========== Render Present ======================================================
    @property
    def renderPointsAsSpheres(self) -> bool: ...
    @renderPointsAsSpheres.setter
    def renderPointsAsSpheres(self, value: bool): ...
    @property
    def renderLinesAsTubes(self) -> bool: ...
    @renderLinesAsTubes.setter
    def renderLinesAsTubes(self, value: bool): ...
    # =========== Selection ======================================================
    @property
    def selectionColor(self) -> tuple[float, float, float, float]: ...
    @selectionColor.setter
    def selectionColor(self, value: tuple[float, float, float, float]): ...
    @property
    def selectionLineWidth(self) -> float: ...
    @selectionLineWidth.setter
    def selectionLineWidth(self, value: float): ...
    @property
    def selectionPointSize(self) -> float: ...
    @selectionPointSize.setter
    def selectionPointSize(self, value: float): ...
    # =========== Mapper ======================================================
    @property
    def mapper(self) -> vtkMapper: ...
    @mapper.setter
    def mapper(self, value: vtkMapper): ...
