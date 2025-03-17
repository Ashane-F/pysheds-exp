try:
    import numba
    _HAS_NUMBA = True
except ModuleNotFoundError:
    _HAS_NUMBA = False
if _HAS_NUMBA:
    from pyshedsash.sview import Raster, ViewFinder, View
else:
    from pyshedsash.pview import Raster, BaseViewFinder, RegularViewFinder, IrregularViewFinder
    from pyshedsash.pview import RegularGridViewer, IrregularGridViewer
