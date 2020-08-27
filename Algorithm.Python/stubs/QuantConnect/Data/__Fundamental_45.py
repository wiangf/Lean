from .__Fundamental_46 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental.MultiPeriodField
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class NormalizedDilutedEPSGrowth(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The growth in the company's Normalized Diluted EPS on a percentage basis.
    
    NormalizedDilutedEPSGrowth(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    FiveYears: float

    OneYear: float

    ThreeMonths: float

    ThreeYears: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedEBITAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBIT less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's standardized
                definition.
    
    NormalizedEBITAsReportedIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedEBITDAAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBITDA less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's
                standardized definition.
    
    NormalizedEBITDAAsReportedIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedEBITDAIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    EBITDA less Total Unusual Items
    
    NormalizedEBITDAIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedIncomeAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be used to fairly measure a
                company's profitability. This is as reported by the company, may be the same or not the same as Morningstar's standardized
                definition.
    
    NormalizedIncomeAsReportedIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This calculation represents earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be
                used to fairly measure a company's profitability. This is calculated using Net Income from Continuing Operations plus/minus any tax
                affected unusual Items and Goodwill Impairments/Write Offs.
    
    NormalizedIncomeIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedNetProfitMargin(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Normalized Income / Total Revenue. A measure of profitability of the company calculated by finding Normalized Net Profit as a
                percentage of Total Revenues.
    
    NormalizedNetProfitMargin(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedOperatingProfitAsReportedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Operating profit adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be used to fairly
                measure a company's profitability. This is as reported by the company, may be the same or not the same as Morningstar's
                standardized definition.
    
    NormalizedOperatingProfitAsReportedIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedPreTaxIncomeIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This calculation represents pre-tax earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This
                can be used to fairly measure a company's profitability. This is calculated using Pre-Tax Income plus/minus any unusual Items and
                Goodwill Impairments/Write Offs.
    
    NormalizedPreTaxIncomeIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NormalizedROIC(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    [Normalized Income + (Interest Expense * (1-Tax Rate))]  / Invested Capital
    
    NormalizedROIC(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class NotesReceivableBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money
                at a future date(s) within one year of the balance sheet date or the normal operating cycle, whichever is longer. Such amount may
                include accrued interest receivable in accordance with the terms of the note. The note also may contain provisions including a
                discount or premium, payable on demand, secured, or unsecured, interest bearing or non-interest bearing, among a myriad of other
                features and characteristics.
    
    NotesReceivableBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]


class OccupancyAndEquipmentIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Includes total expenses of occupancy and equipment. This item is usually only available for bank industry.
    
    OccupancyAndEquipmentIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.MultiPeriodField.PeriodField]
