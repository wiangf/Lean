import typing
import System.Collections.Generic
import System
import QuantConnect.Securities
import QuantConnect.Scheduling
import QuantConnect.Interfaces
import QuantConnect.Data.UniverseSelection
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Algorithm
import QuantConnect
import Python.Runtime
import NodaTime
import datetime

class UniverseSelectionModelPythonWrapper(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that wraps a Python.Runtime.PyObject object
    
    UniverseSelectionModelPythonWrapper(model: PyObject)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass


class USTreasuriesETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following US Treasuries ETFs at their inception date
                2002-07-26   IEF    iShares 7-10 Year Treasury Bond ETF
                2002-07-26   SHY    iShares 1-3 Year Treasury Bond ETF
                2002-07-26   TLT    iShares 20+ Year Treasury Bond ETF
                2007-01-11   SHV    iShares Short Treasury Bond ETF
                2007-01-11   IEI    iShares 3-7 Year Treasury Bond ETF
                2007-01-11   TLH    iShares 10-20 Year Treasury Bond ETF
                2007-12-10   EDV    Vanguard Ext Duration Treasury ETF
                2007-05-30   BIL    SPDR Barclays 1-3 Month T-Bill ETF
                2007-05-30   SPTL   SPDR Portfolio Long Term Treasury ETF
                2008-05-01   TBT    UltraShort Barclays 20+ Year Treasury
                2009-04-16   TMF    Direxion Daily 20-Year Treasury Bull 3X
                2009-04-16   TMV    Direxion Daily 20-Year Treasury Bear 3X
                2009-08-20   TBF    ProShares Short 20+ Year Treasury
                2009-11-23   VGSH   Vanguard Short-Term Treasury ETF
                2009-11-23   VGIT   Vanguard Intermediate-Term Treasury ETF
                2009-11-24   VGLT   Vanguard Long-Term Treasury ETF
                2010-08-06   SCHO   Schwab Short-Term U.S. Treasury ETF
                2010-08-06   SCHR   Schwab Intermediate-Term U.S. Treasury ETF
                2011-12-01   SPTS   SPDR Portfolio Short Term Treasury ETF
                2012-02-24   GOVT   iShares U.S. Treasury Bond ETF
    
    USTreasuriesETFUniverse()
    """

class VolatilityETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """ VolatilityETFUniverse() """


class NullUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides a null implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel
    
    NullUniverseSelectionModel()
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass


class UniverseSelectionModelPythonWrapper(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel, QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that wraps a Python.Runtime.PyObject object
    
    UniverseSelectionModelPythonWrapper(model: PyObject)
    """
    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.List[QuantConnect.Data.UniverseSelection.Universe]:
        pass

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        pass

    @staticmethod # known case of __new__
    def __new__(self, model: Python.Runtime.PyObject) -> None:
        pass
