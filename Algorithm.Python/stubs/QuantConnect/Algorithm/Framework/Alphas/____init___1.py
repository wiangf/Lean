from .____init___2 import *
import typing
import System.Collections.Generic
import System
import QuantConnect.Securities
import QuantConnect.Indicators
import QuantConnect.Data.UniverseSelection
import QuantConnect.Data
import QuantConnect.Algorithm.Framework.Alphas.Serialization
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm
import QuantConnect
import Python.Runtime
import datetime


class INamedModel:
    """
    Provides a marker interface allowing models to define their own names.
                If not specified, the framework will use the model's type name.
                Implementation of this is not required unless you plan on running multiple models
                of the same type w/ different parameters.
    """
    Name: str



class Insight(System.object):
    """
    Defines a alpha prediction for a single symbol generated by the algorithm
    
    Insight(symbol: Symbol, period: TimeSpan, type: InsightType, direction: InsightDirection)
    Insight(symbol: Symbol, period: TimeSpan, type: InsightType, direction: InsightDirection, magnitude: Nullable[float], confidence: Nullable[float], sourceModel: str, weight: Nullable[float])
    Insight(symbol: Symbol, expiryFunc: Func[DateTime, DateTime], type: InsightType, direction: InsightDirection)
    Insight(symbol: Symbol, expiryFunc: Func[DateTime, DateTime], type: InsightType, direction: InsightDirection, magnitude: Nullable[float], confidence: Nullable[float], sourceModel: str, weight: Nullable[float])
    Insight(generatedTimeUtc: DateTime, symbol: Symbol, period: TimeSpan, type: InsightType, direction: InsightDirection, magnitude: Nullable[float], confidence: Nullable[float], sourceModel: str, weight: Nullable[float])
    """
    def Clone(self) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    @staticmethod
    @typing.overload
    def ComputeCloseTime(exchangeHours: QuantConnect.Securities.SecurityExchangeHours, generatedTimeUtc: datetime.datetime, resolution: QuantConnect.Resolution, barCount: int) -> datetime.datetime:
        pass

    @staticmethod
    @typing.overload
    def ComputeCloseTime(exchangeHours: QuantConnect.Securities.SecurityExchangeHours, generatedTimeUtc: datetime.datetime, period: datetime.timedelta) -> datetime.datetime:
        pass

    def ComputeCloseTime(self, *args) -> datetime.datetime:
        pass

    @staticmethod
    def ComputePeriod(exchangeHours: QuantConnect.Securities.SecurityExchangeHours, generatedTimeUtc: datetime.datetime, closeTimeUtc: datetime.datetime) -> datetime.timedelta:
        pass

    @staticmethod
    def FromSerializedInsight(serializedInsight: QuantConnect.Algorithm.Framework.Alphas.Serialization.SerializedInsight) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    @staticmethod
    @typing.overload
    def Group(insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        pass

    @staticmethod
    @typing.overload
    def Group(insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        pass

    def Group(self, *args) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        pass

    def IsActive(self, utcTime: datetime.datetime) -> bool:
        pass

    def IsExpired(self, utcTime: datetime.datetime) -> bool:
        pass

    @staticmethod
    @typing.overload
    def Price(symbol: QuantConnect.Symbol, resolution: QuantConnect.Resolution, barCount: int, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    @staticmethod
    @typing.overload
    def Price(symbol: QuantConnect.Symbol, closeTimeLocal: datetime.datetime, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    @staticmethod
    @typing.overload
    def Price(symbol: QuantConnect.Symbol, period: datetime.timedelta, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    @staticmethod
    @typing.overload
    def Price(symbol: QuantConnect.Symbol, expiryFunc: typing.Callable[[datetime.datetime], datetime.datetime], direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    def Price(self, *args) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        pass

    def SetPeriodAndCloseTime(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, period: datetime.timedelta, type: QuantConnect.Algorithm.Framework.Alphas.InsightType, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, period: datetime.timedelta, type: QuantConnect.Algorithm.Framework.Alphas.InsightType, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, expiryFunc: typing.Callable[[datetime.datetime], datetime.datetime], type: QuantConnect.Algorithm.Framework.Alphas.InsightType, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, expiryFunc: typing.Callable[[datetime.datetime], datetime.datetime], type: QuantConnect.Algorithm.Framework.Alphas.InsightType, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> None:
        pass

    @typing.overload
    def __new__(self, generatedTimeUtc: datetime.datetime, symbol: QuantConnect.Symbol, period: datetime.timedelta, type: QuantConnect.Algorithm.Framework.Alphas.InsightType, direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection, magnitude: typing.Optional[float], confidence: typing.Optional[float], sourceModel: str, weight: typing.Optional[float]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    CloseTimeUtc: datetime.datetime

    Confidence: typing.Optional[float]

    Direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection

    EstimatedValue: float

    GeneratedTimeUtc: datetime.datetime

    GroupId: typing.Optional[System.Guid]

    Id: System.Guid

    Magnitude: typing.Optional[float]

    Period: datetime.timedelta

    ReferenceValue: float

    ReferenceValueFinal: float

    Score: QuantConnect.Algorithm.Framework.Alphas.InsightScore

    SourceModel: str

    Symbol: QuantConnect.Symbol

    Type: QuantConnect.Algorithm.Framework.Alphas.InsightType

    Weight: typing.Optional[float]



class InsightCollection(System.object, System.Collections.IEnumerable, System.Collections.Generic.ICollection[Insight], System.Collections.Generic.IEnumerable[Insight]):
    """
    Provides a collection for managing insights. This type provides collection access semantics
                as well as dictionary access semantics through TryGetValue, ContainsKey, and this[symbol]
    
    InsightCollection()
    """
    def Add(self, item: QuantConnect.Algorithm.Framework.Alphas.Insight) -> None:
        pass

    def AddRange(self, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        pass

    @typing.overload
    def Clear(self) -> None:
        pass

    @typing.overload
    def Clear(self, symbols: typing.List[QuantConnect.Symbol]) -> None:
        pass

    def Clear(self, *args) -> None:
        pass

    def Contains(self, item: QuantConnect.Algorithm.Framework.Alphas.Insight) -> bool:
        pass

    def ContainsKey(self, symbol: QuantConnect.Symbol) -> bool:
        pass

    def CopyTo(self, array: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight], arrayIndex: int) -> None:
        pass

    def GetActiveInsights(self, utcTime: datetime.datetime) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        pass

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        pass

    def GetNextExpiryTime(self) -> typing.Optional[datetime.datetime]:
        pass

    def HasActiveInsights(self, symbol: QuantConnect.Symbol, utcTime: datetime.datetime) -> bool:
        pass

    def Remove(self, item: QuantConnect.Algorithm.Framework.Alphas.Insight) -> bool:
        pass

    def RemoveExpiredInsights(self, utcTime: datetime.datetime) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        pass

    def TryGetValue(self, symbol: QuantConnect.Symbol, insights: typing.List) -> bool:
        pass

    Count: int

    IsReadOnly: bool


    Item: indexer#


class InsightDirection(System.Enum, System.IConvertible, System.IFormattable, System.IComparable):
    """
    Specifies the predicted direction for a insight (price/volatility)
    
    enum InsightDirection, values: Down (-1), Flat (0), Up (1)
    """
    value__: int
    Down: 'InsightDirection'
    Flat: 'InsightDirection'
    Up: 'InsightDirection'


class InsightScore(System.object):
    """
    Defines the scores given to a particular insight
    
    InsightScore()
    InsightScore(direction: float, magnitude: float, updatedTimeUtc: DateTime)
    """
    def GetScore(self, type: QuantConnect.Algorithm.Framework.Alphas.InsightScoreType) -> float:
        pass

    def ToString(self) -> str:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self) -> None:
        pass

    @typing.overload
    def __new__(self, direction: float, magnitude: float, updatedTimeUtc: datetime.datetime) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Direction: float

    IsFinalScore: bool

    Magnitude: float

    UpdatedTimeUtc: datetime.datetime
