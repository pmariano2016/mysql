# coding: utf-8
from sqlalchemy import CHAR, Column, Float, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AccessHour(Base):
    __tablename__ = 'AccessHours'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    AddressUUID = Column(String(36), comment='AddressUUID')
    Type = Column(BIGINT(20), nullable=False, server_default=text("'0'"), comment='Normal or special hours with DoW')
    Starttime = Column(INTEGER(4), nullable=False, comment='start of period in 24 hour style')
    StopTime = Column(INTEGER(4), nullable=False, comment='stop of period in 24 hour format')
    DayOfMonth = Column(INTEGER(2), nullable=False, comment='Day of Month ')
    MonthOfYear = Column(INTEGER(2), nullable=False, comment='Month number Jan=1 Dec=12')
    Year = Column(INTEGER(4), nullable=False, comment='Year in 4 digits')


class Addres(Base):
    __tablename__ = 'Address'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    AddressUUID = Column(String(36), index=True, server_default=text("'0'"), comment='Address UUID')
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    CustomerSiteID = Column(String(64))
    DeptProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Profile or classification for this Address')
    Add_Name = Column(String(64), comment='Arbitrary label for address location')
    GPSLAT = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    GPSLON = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    EntryLAT = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Lattitude value for gate/driveway entry point')
    EntryLON = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Gate/drive entry Longitude value')
    FullAddress = Column(String(256), comment='Temp Field for Reconciling')
    Street1 = Column(String(50), server_default=text("'0'"))
    Street2 = Column(String(50), server_default=text("'0'"))
    AddSuite = Column(String(24), comment='Suite number etc')
    City = Column(String(36))
    State_Province = Column(String(36))
    PostCode = Column(String(12))
    PostCodePlus = Column(String(12))
    Country = Column(String(36))
    Building = Column(String(36), server_default=text("'0'"))
    County_Parrish = Column(String(36))
    AddressExtra = Column(String(36))
    OSMResp = Column(String(36), nullable=False, server_default=text("'FUJITSU'"), comment='OSM Responsibility - if it varies from Fujitsu ')
    AddressNote = Column(String(1024))
    Directions = Column(String(1024))
    MapURI = Column(String(256), comment='http://maps.google.com/maps?q=$latitude,$longitude')
    AccessHours = Column(String(36), server_default=text("'0000-2400'"), comment='Hours of operation or availability to access site')
    AccessDetail = Column(String(1024), comment='Details for access to address')
    AccessPerson = Column(String(36), comment='UUID of access contact')
    KeyDetail = Column(String(1024), comment='Details for keys to address')
    KeyPerson = Column(String(36), comment='UUID of access contact for keys')
    MaintDetail = Column(String(1024), comment='Details for maint svcs at address')
    MaintPerson = Column(String(36), comment='UUID of maint svcs contact')
    PowerDetail = Column(String(1024), comment='Details for power issues at address')
    PowerPerson = Column(String(36), comment='UUID of contact for power issues')
    SiteNOCDetail = Column(String(1024), comment='Details for NOC responsible for address')
    SiteNOCPerson = Column(String(36), comment='UUID of NOC contact')
    SiteWarnings = Column(String(1024), comment='Details for access to address')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User')
    ModDate = Column(BIGINT(20), comment='Date Of Last Modification')
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User to make  last modification')


class AddressEe(Base):
    __tablename__ = 'Address_ee'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    AddressUUID = Column(String(36), index=True, server_default=text("'0'"), comment='Address UUID')
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    CustomerSiteID = Column(String(64))
    DeptProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Profile or classification for this Address')
    Add_Name = Column(String(64), comment='Arbitrary label for address location')
    GPSLAT = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    GPSLON = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    EntryLAT = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Lattitude value for gate/driveway entry point')
    EntryLON = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Gate/drive entry Longitude value')
    FullAddress = Column(String(256), comment='Temp Field for Reconciling')
    Street1 = Column(String(50), server_default=text("'0'"))
    Street2 = Column(String(50), server_default=text("'0'"))
    AddSuite = Column(String(24), comment='Suite number etc')
    City = Column(String(36))
    State_Province = Column(String(36))
    PostCode = Column(String(12))
    PostCodePlus = Column(String(12))
    Country = Column(String(36))
    Building = Column(String(36), server_default=text("'0'"))
    County_Parrish = Column(String(36))
    AddressExtra = Column(String(36))
    OSMResp = Column(String(36), nullable=False, server_default=text("'FUJITSU'"), comment='OSM Responsibility - if it varies from Fujitsu ')
    AddressNote = Column(String(1024))
    Directions = Column(String(1024))
    MapURI = Column(String(256), comment='http://maps.google.com/maps?q=$latitude,$longitude')
    AccessHours = Column(String(36))
    AccessDetail = Column(String(1024), comment='Details for access to address')
    AccessPerson = Column(String(36), comment='UUID of access contact')
    KeyDetail = Column(String(1024), comment='Details for keys to address')
    KeyPerson = Column(String(36), comment='UUID of access contact for keys')
    MaintDetail = Column(String(1024), comment='Details for maint svcs at address')
    MaintPerson = Column(String(36), comment='UUID of maint svcs contact')
    PowerDetail = Column(String(1024), comment='Details for power issues at address')
    PowerPerson = Column(String(36), comment='UUID of contact for power issues')
    SiteNOCDetail = Column(String(1024), comment='Details for NOC responsible for address')
    SiteNOCPerson = Column(String(36), comment='UUID of NOC contact')
    SiteWarnings = Column(String(1024), comment='Details for access to address')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User')
    ModDate = Column(BIGINT(20), comment='Date Of Last Modification')
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User to make  last modification')


class AddressSz(Base):
    __tablename__ = 'Address_sz'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    AddressUUID = Column(String(36), index=True, server_default=text("'0'"), comment='Address UUID')
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    CustomerSiteID = Column(String(64))
    DeptProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Profile or classification for this Address')
    Add_Name = Column(String(64), comment='Arbitrary label for address location')
    GPSLAT = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    GPSLON = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    EntryLAT = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Lattitude value for gate/driveway entry point')
    EntryLON = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Gate/drive entry Longitude value')
    FullAddress = Column(String(256), comment='Temp Field for Reconciling')
    Street1 = Column(String(50), server_default=text("'0'"))
    Street2 = Column(String(50), server_default=text("'0'"))
    AddSuite = Column(String(24), comment='Suite number etc')
    City = Column(String(36))
    State_Province = Column(String(36))
    PostCode = Column(String(12))
    PostCodePlus = Column(String(12))
    Country = Column(String(36))
    Building = Column(String(36), server_default=text("'0'"))
    County_Parrish = Column(String(36))
    AddressExtra = Column(String(36))
    OSMResp = Column(String(36), nullable=False, server_default=text("'FUJITSU'"), comment='OSM Responsibility - if it varies from Fujitsu ')
    AddressNote = Column(String(1024))
    Directions = Column(String(1024))
    MapURI = Column(String(256), comment='http://maps.google.com/maps?q=$latitude,$longitude')
    AccessHours = Column(String(36))
    AccessDetail = Column(String(1024), comment='Details for access to address')
    AccessPerson = Column(String(36), comment='UUID of access contact')
    KeyDetail = Column(String(1024), comment='Details for keys to address')
    KeyPerson = Column(String(36), comment='UUID of access contact for keys')
    MaintDetail = Column(String(1024), comment='Details for maint svcs at address')
    MaintPerson = Column(String(36), comment='UUID of maint svcs contact')
    PowerDetail = Column(String(1024), comment='Details for power issues at address')
    PowerPerson = Column(String(36), comment='UUID of contact for power issues')
    SiteNOCDetail = Column(String(1024), comment='Details for NOC responsible for address')
    SiteNOCPerson = Column(String(36), comment='UUID of NOC contact')
    SiteWarnings = Column(String(1024), comment='Details for access to address')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User')
    ModDate = Column(BIGINT(20), comment='Date Of Last Modification')
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User to make  last modification')


class AddressZ(Base):
    __tablename__ = 'Address_z'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    AddressUUID = Column(String(36), index=True, server_default=text("'0'"), comment='Address UUID')
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    CustomerSiteID = Column(String(64))
    DeptProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Profile or classification for this Address')
    Add_Name = Column(String(64), comment='Arbitrary label for address location')
    GPSLAT = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    GPSLON = Column(Float(16, True), index=True, server_default=text("'0.00000000'"))
    EntryLAT = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Lattitude value for gate/driveway entry point')
    EntryLON = Column(Float(16, True), server_default=text("'0.00000000'"), comment='Gate/drive entry Longitude value')
    FullAddress = Column(String(256), comment='Temp Field for Reconciling')
    Street1 = Column(String(50), server_default=text("'0'"))
    Street2 = Column(String(50), server_default=text("'0'"))
    AddSuite = Column(String(24), comment='Suite number etc')
    City = Column(String(36))
    State_Province = Column(String(36))
    PostCode = Column(String(12))
    PostCodePlus = Column(String(12))
    Country = Column(String(36))
    Building = Column(String(36), server_default=text("'0'"))
    County_Parrish = Column(String(36))
    AddressExtra = Column(String(36))
    OSMResp = Column(String(36), nullable=False, server_default=text("'FUJITSU'"), comment='OSM Responsibility - if it varies from Fujitsu ')
    AddressNote = Column(String(1024))
    Directions = Column(String(1024))
    MapURI = Column(String(256), comment='http://maps.google.com/maps?q=$latitude,$longitude')
    AccessHours = Column(String(36))
    AccessDetail = Column(String(1024), comment='Details for access to address')
    AccessPerson = Column(String(36), comment='UUID of access contact')
    KeyDetail = Column(String(1024), comment='Details for keys to address')
    KeyPerson = Column(String(36), comment='UUID of access contact for keys')
    MaintDetail = Column(String(1024), comment='Details for maint svcs at address')
    MaintPerson = Column(String(36), comment='UUID of maint svcs contact')
    PowerDetail = Column(String(1024), comment='Details for power issues at address')
    PowerPerson = Column(String(36), comment='UUID of contact for power issues')
    SiteNOCDetail = Column(String(1024), comment='Details for NOC responsible for address')
    SiteNOCPerson = Column(String(36), comment='UUID of NOC contact')
    SiteWarnings = Column(String(1024), comment='Details for access to address')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User')
    ModDate = Column(BIGINT(20), comment='Date Of Last Modification')
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User to make  last modification')


class AlarmType(Base):
    __tablename__ = 'AlarmType'

    UniqueID = Column(INTEGER(16), primary_key=True)
    UUID = Column(String(36))
    AlarmTypeText = Column(String(128), comment='Alarm text from alarm message LOC LOS etc.')
    AIDType = Column(String(64), comment='What module generates this type of message')
    Direction = Column(String(36), comment='Direction of fault if any')
    AlarmTypeDescription = Column(String(1024), comment='What does the alarm mean?')
    AlarmTypeRemedy = Column(String(2048), comment='Steps to remedy this alarm')
    AlarmTypeModel = Column(String(50), nullable=False, server_default=text("'0'"))
    AlarmTypeVendor = Column(String(50))
    HelpURL = Column(String(1024), comment='URL for online help if any is available')
    AlarmTypeSeverity = Column(INTEGER(8), comment='Severity associated with this type of alarm')
    AlarmTypeNote = Column(String(256), comment='Notes about this alarm type')
    SourceVersion = Column(String(64), comment='Where did this information come from and version info')
    ModDate = Column(BIGINT(20), comment='Date of last modification')
    ModUser = Column(INTEGER(12))
    CreateDate = Column(BIGINT(20), comment='Date record was added - set on create')
    CreateUser = Column(String(36), comment='User ID of person who added this record')


t_CSWI_Escalation = Table(
    'CSWI_Escalation', metadata,
    Column('CSWIID', String(36), index=True, server_default=text("'0'")),
    Column('ContactOrder', INTEGER(11), server_default=text("'0'")),
    Column('ContactCard', String(36), server_default=text("'0'"))
)


class CSWIMeta(Base):
    __tablename__ = 'CSWI_Meta'

    CSWIID = Column(String(36), primary_key=True, server_default=text("'0'"))
    Overview = Column(String(5000), server_default=text("''"))
    SupportedServices = Column(String(36), server_default=text("'0'"))
    EscalationList = Column(String(36), server_default=text("'0'"))
    EquipmentList = Column(String(36), server_default=text("'0'"))
    NetworkTopology = Column(String(50), server_default=text("'0'"))
    ServiceLevelObjective = Column(String(36), server_default=text("'0'"))
    ReferenceMaterial = Column(String(36), server_default=text("'0'"))


t_CSWI_Services = Table(
    'CSWI_Services', metadata,
    Column('CSWIID', String(36), index=True, server_default=text("'0'")),
    Column('NOCService', String(20), server_default=text("''")),
    Column('ServiceLevelAgreement', String(20), server_default=text("'0'")),
    Column('Vendor', String(36), server_default=text("'0'"))
)


class CircuitDatum(Base):
    __tablename__ = 'CircuitData'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')


class Company(Base):
    __tablename__ = 'Company'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36), index=True)
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this company associated with')
    CustAcct = Column(String(24), comment='Customer Account Number if applicable')
    CompanyName = Column(String(64), comment='Arbitrary label for company name or display name')
    CoProfile = Column(INTEGER(16), server_default=text("'0'"), comment='No known Use')
    CompanyURL = Column(String(1024), comment='URL of company Website')
    CoAddUUID = Column(String(36), comment='UUID of Company Address')
    Note = Column(String(256))
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    ModDate = Column(BIGINT(20))
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class Contact(Base):
    __tablename__ = 'Contacts'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36), index=True)
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    CustomerAccount = Column(String(36), comment="Our customer's customer account number")
    ContactProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Profile or classification ID for this contact')
    Name_Label = Column(String(64), index=True, comment='Descriptive label or name')
    FirstName = Column(String(24), server_default=text("'0'"))
    LastName = Column(String(24), server_default=text("'0'"))
    Prefix = Column(String(12), server_default=text("'0'"), comment='Mr Mrs Ms etc')
    Title = Column(String(64), server_default=text("'0'"))
    Role = Column(String(64), server_default=text("'0'"), comment='Description of persons role')
    BussAdd1 = Column(String(36), comment='UUID to 1st buss address')
    BussAdd2 = Column(String(36), comment='UUID to 2st buss address')
    DeliveryAdd = Column(String(36), comment='UUID to delivery address')
    HomeAddress = Column(String(36), comment='UUID to home address')
    BussEmail = Column(String(64), comment='business email address')
    PersEmail = Column(String(64), comment='personal email address')
    AltEmail = Column(String(64), comment='alternate email address')
    BussPhone1 = Column(String(16))
    BussExt1 = Column(String(8))
    BussPhone2 = Column(String(16))
    BussExt2 = Column(String(8))
    BussFax = Column(String(16))
    Mobile = Column(String(16))
    Pager = Column(String(16))
    Voicemail = Column(String(16))
    Admin = Column(String(36), comment='UUID of admin contact record')
    Company = Column(String(36), comment='UUID of company contact record')
    BussGroup = Column(String(64), comment='UUID of bussiness group contact')
    AltPerson = Column(String(36), comment='UUID of alternate contact')
    EscPerson = Column(String(36), comment='UUID of list of escalation contacts records')
    ContactNote = Column(String(1024))
    CreateDate = Column(BIGINT(20), comment='Epoch Date this record was added')
    CreateUser = Column(INTEGER(10), comment='User ID that created this record')
    ModDate = Column(BIGINT(20), comment='Epoch Date this record was last modified')
    ModUser = Column(INTEGER(10), comment='User ID of last user to modify this record')


class ContactsEe(Base):
    __tablename__ = 'Contacts_ee'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36), index=True)
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    CustomerAccount = Column(String(36), comment="Our customer's customer account number")
    ContactProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Profile or classification ID for this contact')
    Name_Label = Column(String(64), index=True, comment='Descriptive label or name')
    FirstName = Column(String(24), server_default=text("'0'"))
    LastName = Column(String(24), server_default=text("'0'"))
    Prefix = Column(String(12), server_default=text("'0'"), comment='Mr Mrs Ms etc')
    Title = Column(String(64), server_default=text("'0'"))
    Role = Column(String(64), server_default=text("'0'"), comment='Description of persons role')
    BussAdd1 = Column(String(36), comment='UUID to 1st buss address')
    BussAdd2 = Column(String(36), comment='UUID to 2st buss address')
    DeliveryAdd = Column(String(36), comment='UUID to delivery address')
    HomeAddress = Column(String(36), comment='UUID to home address')
    BussEmail = Column(String(64), comment='business email address')
    PersEmail = Column(String(64), comment='personal email address')
    AltEmail = Column(String(64), comment='alternate email address')
    BussPhone1 = Column(String(16))
    BussExt1 = Column(String(8))
    BussPhone2 = Column(String(16))
    BussExt2 = Column(String(8))
    BussFax = Column(String(16))
    Mobile = Column(String(16))
    Pager = Column(String(16))
    Voicemail = Column(String(16))
    Admin = Column(String(36), comment='UUID of admin contact record')
    Company = Column(String(36), comment='UUID of company contact record')
    BussGroup = Column(String(64), comment='UUID of bussiness group contact')
    AltPerson = Column(String(36), comment='UUID of alternate contact')
    EscPerson = Column(String(36), comment='UUID of list of escalation contacts records')
    ContactNote = Column(String(1024))
    CreateDate = Column(BIGINT(20), comment='Epoch Date this record was added')
    CreateUser = Column(INTEGER(10), comment='User ID that created this record')
    ModDate = Column(BIGINT(20), comment='Epoch Date this record was last modified')
    ModUser = Column(INTEGER(10), comment='User ID of last user to modify this record')


class CxLog(Base):
    __tablename__ = 'CxLog'

    UniqueID = Column(INTEGER(16), primary_key=True)
    LogUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogCktID = Column(String(128), index=True, comment='Label value for reports etc')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    DMPPeerUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    Contact = Column(String(36), comment='Address contact UUID')
    COS = Column(INTEGER(12), comment='Class Of Service')
    ModDate = Column(BIGINT(20), comment='Date of last modification')
    ModUser = Column(INTEGER(12))
    CreateDate = Column(BIGINT(20), comment='Date record was added - set on create')
    CreateUser = Column(String(36), comment='User ID of person who added this record')


class DAT(Base):
    __tablename__ = 'DAT'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')
    Smoothing = Column(INTEGER(10))


class DATTest(Base):
    __tablename__ = 'DAT_Test'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')


class DATEe(Base):
    __tablename__ = 'DAT_ee'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')


class DATKev(Base):
    __tablename__ = 'DAT_kev'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')
    Smoothing = Column(INTEGER(10))


class DATSz(Base):
    __tablename__ = 'DAT_sz'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')
    Smoothing = Column(INTEGER(10))


class DMPPeer(Base):
    __tablename__ = 'DMPPeer'

    UniqueID = Column(INTEGER(10), primary_key=True)
    UUID = Column(String(36), unique=True)
    A_DMP_UUID = Column(String(36), nullable=False, server_default=text("'0'"))
    Z_DMP_UUID = Column(String(36))
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    Description = Column(String(128), comment='Description of this DMP+Peer ckt by use or name etc.')
    BW_Down = Column(Float, server_default=text("'0'"), comment='Bandwidth allocation Z to A in megabits')
    BW_Up = Column(Float, server_default=text("'0'"))
    COS = Column(INTEGER(12), comment='Class of Service')
    NetworkProfile = Column(INTEGER(20))
    EndUserRef = Column(String(128), comment='Just a label for reports')
    SubUUID = Column(String(36), comment='Subscriber UUID from subscriber table')
    Contact = Column(String(36), comment='Owner or manager type contact')
    FiberPrimary = Column(String(128), comment='Primary fiber cable assignment')
    FiberSecondary = Column(String(128), comment='Secondary fiber assignment')
    FiberSitePrimary = Column(String(128), comment='primary site fiber assignment')
    FiberSiteSecondary = Column(String(128), comment='Secondary site fiber assignment')
    CarrierUUID = Column(String(64), comment='Contact UUID for carrier')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(12))
    ModDate = Column(BIGINT(20))
    ModUser = Column(INTEGER(12))
    CarrierRef = Column(String(64), comment='Carrier circuit ID or ref')


class DMPPeerTest(Base):
    __tablename__ = 'DMPPeer_Test'

    UniqueID = Column(INTEGER(10), primary_key=True)
    UUID = Column(String(36), server_default=text("''"))
    A_DMP_UUID = Column(String(36), nullable=False, server_default=text("''"))
    Z_DMP_UUID = Column(String(36), server_default=text("''"))
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    Description = Column(String(128), server_default=text("''"), comment='Description of this DMP+Peer ckt by use or name etc.')
    Protocol = Column(String(64), comment='WDM ETH etc.')
    BW_Down = Column(INTEGER(10), server_default=text("'0'"), comment='Bandwidth allocation Z to A in megabits')
    BW_Up = Column(INTEGER(10), server_default=text("'0'"), comment='Bandwidth allocation A to Z in megabits')
    COS = Column(INTEGER(12), server_default=text("'0'"), comment='Class of Service')
    NetworkProfile = Column(INTEGER(20), server_default=text("'0'"))
    EndUserRef = Column(String(128), server_default=text("''"), comment='Just a label for reports')
    SubscriberUUID = Column(String(36), server_default=text("''"), comment='Subscriber UUID from subscriber table')
    Contact = Column(String(36), server_default=text("''"), comment='Owner or manager type contact')
    FiberPrimary = Column(String(128), server_default=text("''"), comment='Primary fiber cable assignment')
    FiberPrimary_TX = Column(String(20), server_default=text("''"), comment='Transmit fiber designator')
    FiberPrimary_RX = Column(String(20), server_default=text("''"), comment='Receive fiber designator')
    FiberSecondary = Column(String(128), server_default=text("''"), comment='Secondary fiber assignment')
    FiberSecondary_TX = Column(String(20), server_default=text("''"), comment='Transmit fiber designator')
    FiberSecondary_RX = Column(String(20), server_default=text("''"), comment='Receive fiber designator')
    FiberSitePrimary = Column(String(128), server_default=text("''"), comment='primary site fiber assignment')
    FiberSitePrimary_TX = Column(String(20), server_default=text("''"), comment='Transmit fiber designator')
    FiberSitePrimary_RX = Column(String(20), server_default=text("''"), comment='Receive fiber designator')
    FiberSiteSecondary = Column(String(128), server_default=text("''"), comment='Secondary site fiber assignment')
    FiberSiteSecondary_TX = Column(String(20), server_default=text("''"), comment='Transmit fiber designator')
    FiberSiteSecondary_RX = Column(String(20), server_default=text("''"), comment='Receive fiber designator')
    CarrierUUID = Column(String(64), server_default=text("'0'"), comment='Contact UUID for carrier')
    CarrierRef = Column(String(64), server_default=text("''"), comment='Carrier circuit ID or ref')
    Note = Column(String(512), comment='Comments about DMPPeer circuit')
    CreateDate = Column(BIGINT(20), server_default=text("'0'"))
    CreateUser = Column(INTEGER(12), server_default=text("'0'"))
    ModDate = Column(BIGINT(20), server_default=text("'0'"))
    ModUser = Column(INTEGER(12), server_default=text("'0'"))


class DMPPeerEe(Base):
    __tablename__ = 'DMPPeer_ee'

    UniqueID = Column(INTEGER(10), primary_key=True)
    UUID = Column(String(36), unique=True)
    A_DMP_UUID = Column(String(36), nullable=False, server_default=text("'0'"))
    Z_DMP_UUID = Column(String(36))
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    Description = Column(String(128), comment='Description of this DMP+Peer ckt by use or name etc.')
    BW_Down = Column(Float, server_default=text("'0'"), comment='Bandwidth allocation Z to A in megabits')
    BW_Up = Column(Float, server_default=text("'0'"))
    COS = Column(INTEGER(12), comment='Class of Service')
    NetworkProfile = Column(INTEGER(20))
    EndUserRef = Column(String(128), comment='Just a label for reports')
    SubUUID = Column(String(36), comment='Subscriber UUID from subscriber table')
    Contact = Column(String(36), comment='Owner or manager type contact')
    FiberPrimary = Column(String(128), comment='Primary fiber cable assignment')
    FiberSecondary = Column(String(128), comment='Secondary fiber assignment')
    FiberSitePrimary = Column(String(128), comment='primary site fiber assignment')
    FiberSiteSecondary = Column(String(128), comment='Secondary site fiber assignment')
    CarrierUUID = Column(String(64), comment='Contact UUID for carrier')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(12))
    ModDate = Column(BIGINT(20))
    ModUser = Column(INTEGER(12))
    CarrierRef = Column(String(64), comment='Carrier circuit ID or ref')


class DeptCode(Base):
    __tablename__ = 'DeptCode'
    __table_args__ = (
        Index('DeptCode', 'DeptCode', 'DepUUID', 'DeptName'),
    )

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    DeptCode = Column(BIGINT(20), nullable=False, server_default=text("'0'"), comment='Code number for this department')
    DeptName = Column(String(36), index=True, comment='Arbitrary Name for the department code')
    DeptDescription = Column(String(64), comment='Description for this department code')
    DeptPriority = Column(BIGINT(20), nullable=False, server_default=text("'1'"), comment='Priority for the department')
    AccountID = Column(String(20), comment='Matches AccountID from DAT table')
    ModDate = Column(INTEGER(10), comment='Date Of Last Modification')
    DepUUID = Column(String(36), comment='Department code UUID')


class Inventory(Base):
    __tablename__ = 'Inventory'

    UniqueID = Column(INTEGER(11), primary_key=True)
    TID = Column(String(64), nullable=False)
    UUID = Column(String(36), nullable=False)
    IPAddress = Column(String(20))
    serial = Column(String(65))
    software = Column(String(65))
    model = Column(String(128))
    Description = Column(String(64))


class MODAT(Base):
    __tablename__ = 'MODAT'

    UniqueID = Column(INTEGER(4), primary_key=True, comment='Unique record ID')
    RecID = Column(INTEGER(4), nullable=False, server_default=text("'0'"), comment='Record ID')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"), comment='Universal Unique ID')
    DisplayName = Column(String(128), comment='Arbitrary Module Name Label for Display purposes')
    DeptID = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Lookup ID for Department Info')
    MainFlag = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Main module has system IP and version information')
    ModType = Column(String(64), comment='MAIN Chassis Card Module MOBO etc.')
    ModManufacturer = Column(String(64), comment='Name of manufacturer')
    ModSerial = Column(String(64), comment='Serial number of the module')
    Clock = Column(String(64))
    HWRev = Column(String(64), comment='Hardware revision number')
    FirmWareRev = Column(String(64))
    ModModel = Column(String(64), comment='Model number of the module')
    ModOSName = Column(String(64), comment='Name of the OS for the Module if applicable')
    ModOSVers = Column(String(64), comment='Version of the OS for this module if applicable')
    ModOSDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the OS version was installed on module')
    ModCategory = Column(String(64), comment='optical data etc')
    ModClass = Column(String(64), comment='small medium large etc')
    ModShelf = Column(String(10), nullable=False, server_default=text("'0'"), comment='Shelf number the module is installed on - default is 0 for no shelves')
    ModSlot = Column(String(10), nullable=False, server_default=text("'0'"), comment='Slot number the module is installed in - default is 0 for no slots')
    EquipType = Column(String(64), comment='Type of module - varies by NE and manufacturer')
    Manufacturer = Column(String(64), comment='Name of device manufacturer')
    NE_Model = Column(String(64), comment='Model name of the device')
    ModPartNo = Column(String(64))
    NE_OSName = Column(String(64), comment='Name of the installed OS')
    NE_OSVers = Column(String(64), comment='version of the installed OS')
    RFODate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the module is ready for Operation - can generate alarms')
    RFMDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the module is ready for Monitoring - is clean of standing alarms')
    RFSDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the module is ready for traffic - live billable traffic')
    DecDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the module is decommissioned')
    MTODate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the module is marked MTO - When NOC began monitoring')
    ADDDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date record was added to DB')
    AddUser = Column(SMALLINT(5), nullable=False, server_default=text("'0'"), comment='User ID that added record')
    MODDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date of last change to record')
    ModUser = Column(SMALLINT(5), nullable=False, server_default=text("'0'"), comment='User ID that modified record last')
    Status = Column(String(24), nullable=False, server_default=text("'Unknown'"), comment='current status of the module')
    IPAddress = Column(String(20), comment='IP Address of NE if applicable')
    GatewayIP = Column(String(20), comment='IP Address of GNE if applicable')
    SubnetAdd = Column(String(20), comment='Subnet of device if applicable')
    MACAdd = Column(String(20), comment='MAC Address of device if applicable')
    GNEIP = Column(String(20), comment='IP Address of GNE if applicable')
    GNEGateway = Column(String(20), comment='IP Address of GNE if applicable')
    GNESubnet = Column(String(20), comment='Subnet of GNE if applicable')
    GNEMACAdd = Column(String(20), comment='GNE MAC Address if applicable')
    SoftwareRev = Column(String(64))
    NEUUID = Column(String(36), comment='UUID of parent NE')


class NEAT(Base):
    __tablename__ = 'NEAT'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    RecID = Column(INTEGER(4), nullable=False, server_default=text("'0'"), comment='Record ID')
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"), comment='Universal Unique ID')
    TID = Column(CHAR(64), index=True, comment='The TID name')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')
    CustomerType = Column(String(24), comment='NOC, HEMS etc')
    Customer = Column(String(64), comment='Customer Name')
    Subscriber = Column(String(64), comment='Customer subscriber name')
    NetworkGroup = Column(String(64), comment='IE NS1500 partition etc')
    NEProfile = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Category or classification for the NE')
    SiteName = Column(String(64), comment='FNC ID or other site identifier')
    AddressUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    AccountID = Column(String(32), comment='SAP account ID applicable for this Customer/Subscriber combination')
    GPSLoc = Column(BIGINT(20), server_default=text("'0'"), comment='Lookup Value For GPS/Address Table')
    OSMInfo = Column(String(64), comment='OSM information for this NE')
    NESiteClass = Column(String(64), comment='Classification - DC Crit1 Crit2 etc')
    RFODate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the NE is ready for Operation - can generate alarms')
    RFMDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the NE is ready for Monitoring - is clean of standing alarms')
    RFSDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the NE is ready for traffic - live billable traffic')
    MTODate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the NE is marked MTO - When NOC began monitoring')
    DecDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the NE is decommissioned')
    ADDDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date record was added to DB')
    AddUser = Column(SMALLINT(5), nullable=False, server_default=text("'0'"), comment='User ID that added record')
    MODDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date of last change to record')
    ModUser = Column(SMALLINT(5), nullable=False, server_default=text("'0'"), comment='User ID that modified record last')
    Status = Column(String(24), nullable=False, server_default=text("'Unknown'"), comment='current status of the NE - RFM MTO DECO etc')
    NE_Type = Column(String(64), comment='EquipmentType Depends on OEM classification')
    NE_Manufacturer = Column(String(64), comment='Name of device manufacturer')
    NE_Model = Column(String(64), comment='Model name of the device')
    NE_ServiceTag = Column(String(36), comment='Service Tag Info from NE')
    NE_SerialNo = Column(String(36))
    NE_OSName = Column(String(64), comment='Name of the installed OS')
    NE_HWRev = Column(String(64), comment='Hardware revision')
    NE_OSVers = Column(String(64), comment='version of the installed OS')
    NE_OSVerDate = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Epoch Date the OS was installed')
    NE_Category = Column(String(64), comment='optical data etc')
    NE_Class = Column(String(64), comment='small medium large etc')
    NE_Note = Column(String(1024))


class NOCClient(Base):
    __tablename__ = 'NOCClient'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36))
    CustomerName = Column(String(64))
    SubscriberName = Column(String(64), comment='Customer Account Number if applicable')
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this company associated with')
    SpecialInstructionURI = Column(String(1024), comment='URL information for CSWI')
    x0 = Column(INTEGER(16), server_default=text("'0'"), comment='No known Use')
    x1 = Column(String(64), comment='No known use')
    x2 = Column(String(64), server_default=text("'0'"), comment='No known use')
    Note = Column(String(1024))
    CreateDate = Column(BIGINT(20), comment='Epoch date of record creation')
    CreateUser = Column(INTEGER(10), comment='User ID that created this record')
    ModDate = Column(BIGINT(20), comment='Epoch time of last modification')
    ModUser = Column(INTEGER(10), comment='User ID of last person to change this record')


class Object(Base):
    __tablename__ = 'Object'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    ObjectUUID = Column(String(36), index=True, server_default=text("'0'"), comment='Address UUID')
    AcctAssoc = Column(String(24), index=True, server_default=text("'0'"), comment='What account is this address associated with')
    ObjectProfile = Column(String(32), index=True, server_default=text("'0'"), comment='Category or profile classification for this object')
    ObjectName = Column(String(64), comment='Arbitrary label for object')
    All_TID = Column(String(36), server_default=text("'0'"), comment='UUID for All TIDs record')
    Address = Column(String(36), server_default=text("'0'"), comment='UUID for Address record')
    FloorLabel = Column(String(36), server_default=text("'0'"))
    FloorDetail = Column(String(256))
    FloorContact = Column(String(36), comment='UUID for contact for this floor')
    RoomLabel = Column(String(36))
    RoomDetail = Column(String(256))
    RoomContact = Column(String(36), comment='UUID for contact for this room')
    CageLabel = Column(String(36))
    CageDetail = Column(String(256))
    CageContact = Column(String(36), comment='UUID to contact for this cage')
    RackLabel = Column(String(36))
    RackDetail = Column(String(256))
    RackContact = Column(String(36), comment='UUID to contact for this rack')
    Top_RU_Num = Column(INTEGER(4), server_default=text("'0'"), comment='top most RU number in rack for equipment/shelf')
    ObjectNote = Column(String(1024))


class OpenHour(Base):
    __tablename__ = 'OpenHours'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    UUID = Column(String(36), comment='UUID')
    Type = Column(BIGINT(20), nullable=False, server_default=text("'0'"), comment='Opening Hours Index')
    Description = Column(String(64), nullable=False, comment='Text of opening hours')


class Subscriber(Base):
    __tablename__ = 'Subscriber'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36))
    SubscriberName = Column(String(64), index=True, comment='Customer Account Number if applicable')
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this company associated with')
    SpecialInstructionURI = Column(String(1024), comment='URL information for CSWI')
    SubActive = Column(INTEGER(16), nullable=False, server_default=text("'0'"), comment='Active status of this record/company/subscriber')
    x1 = Column(String(64), comment='No known use')
    x2 = Column(String(64), server_default=text("'0'"), comment='No known use')
    Note = Column(String(1024))
    CreateDate = Column(BIGINT(20), comment='Epoch date of record creation')
    CreateUser = Column(INTEGER(10), comment='User ID that created this record')
    ModDate = Column(BIGINT(20), comment='Epoch time of last modification')
    ModUser = Column(INTEGER(10), comment='User ID of last person to change this record')


class SubscriberTest(Base):
    __tablename__ = 'Subscriber_Test'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36))
    SubscriberName = Column(String(64), index=True, comment='Customer Account Number if applicable')
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this company associated with')
    SpecialInstructionURI = Column(String(1024), comment='URL information for CSWI')
    SubActive = Column(INTEGER(16), nullable=False, server_default=text("'0'"), comment='Active status of this record/company/subscriber')
    x1 = Column(String(64), comment='No known use')
    x2 = Column(String(64), server_default=text("'0'"), comment='No known use')
    Note = Column(String(1024))
    CreateDate = Column(BIGINT(20), comment='Epoch date of record creation')
    CreateUser = Column(INTEGER(10), comment='User ID that created this record')
    ModDate = Column(BIGINT(20), comment='Epoch time of last modification')
    ModUser = Column(INTEGER(10), comment='User ID of last person to change this record')


class SvcLog(Base):
    __tablename__ = 'SvcLog'

    UniqueID = Column(INTEGER(16), primary_key=True)
    LogUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogCktID = Column(String(128), index=True, comment='Label value for reports etc')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    DMPPeerUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    Contact = Column(String(36), comment='Address contact UUID')
    COS = Column(INTEGER(12), comment='Class Of Service')
    ModDate = Column(BIGINT(20), comment='Date of last modification')
    ModUser = Column(INTEGER(12))
    CreateDate = Column(BIGINT(20), comment='Date record was added - set on create')
    CreateUser = Column(String(36), comment='User ID of person who added this record')


class SvcLogTest(Base):
    __tablename__ = 'SvcLog_Test'

    UniqueID = Column(INTEGER(16), primary_key=True)
    LogUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogCktID = Column(String(128), index=True, comment='Label value for reports etc')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    DMPPeerUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    Contact = Column(String(36), comment='Address contact UUID')
    COS = Column(INTEGER(12), comment='Class Of Service')
    ModDate = Column(BIGINT(20), comment='Date of last modification')
    ModUser = Column(INTEGER(12))
    CreateDate = Column(BIGINT(20), comment='Date record was added - set on create')
    CreateUser = Column(String(36), comment='User ID of person who added this record')


class SvcVir(Base):
    __tablename__ = 'SvcVir'

    UniqueID = Column(INTEGER(16), primary_key=True)
    VirUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    VirCktID = Column(String(128), comment='End User circuit reference')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SvcLogWorkUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    BW_Down = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Bandwidth Allocation Down - Z to A')
    BW_Up = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Bandwidth Allocation Up - A to Z')
    EndUserRef = Column(String(128), comment='End user reference for this circuit')
    SvcLogProtUUID = Column(String(36))
    COS = Column(INTEGER(12), comment='Class of Service')
    Contact = Column(String(36), comment='Owner or manager / technical type contact UUID')
    EndUserID = Column(String(128), comment='End User ID replaces FNC ID')
    EndUser = Column(String(36), comment='EndUser Contact record / Company UUID')
    Description = Column(String(128), comment='Description of this virtual ckt by use or name etc.')
    DeptID = Column(INTEGER(20))
    CreateDate = Column(INTEGER(11), nullable=False, comment='Epoch date that record was created')
    CreateUser = Column(INTEGER(10), nullable=False, comment='User id that created this record')
    ModDate = Column(INTEGER(10), nullable=False, comment='Epoch date this record was last modified')
    ModUser = Column(INTEGER(10), nullable=False, comment='User ID of last modification')


class SvcVirTest(Base):
    __tablename__ = 'SvcVir_test'

    UniqueID = Column(INTEGER(16), primary_key=True)
    VirUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    VirCktID = Column(String(128), comment='End User circuit reference')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SvcLogWorkUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    BW_Down = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Bandwidth Allocation Down - Z to A')
    BW_Up = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Bandwidth Allocation Up - A to Z')
    EndUserRef = Column(String(128), comment='End user reference for this circuit')
    SvcLogProtUUID = Column(String(36))
    COS = Column(INTEGER(12), comment='Class of Service')
    Contact = Column(String(36), comment='Owner or manager / technical type contact UUID')
    EndUserID = Column(String(128), comment='End User ID replaces FNC ID')
    EndUser = Column(String(36), comment='EndUser Contact record / Company UUID')
    Description = Column(String(128), comment='Description of this virtual ckt by use or name etc.')
    DeptID = Column(INTEGER(20))
    CreateDate = Column(INTEGER(11), nullable=False, comment='Epoch date that record was created')
    CreateUser = Column(INTEGER(10), nullable=False, comment='User id that created this record')
    ModDate = Column(INTEGER(10), nullable=False, comment='Epoch date this record was last modified')
    ModUser = Column(INTEGER(10), nullable=False, comment='User ID of last modification')


class TicketFlag(Base):
    __tablename__ = 'TicketFlag'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    TicketAction = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"), comment='Ticket Handling code')
    TicketActionName = Column(String(64), comment='Description of ticket action code')
    TicketActionDescr = Column(String(64))
    TicketActionPriority = Column(BIGINT(20), nullable=False, server_default=text("'1'"), comment='Priority for the Action - separate coding')
    TicketActionAcnt = Column(String(20), comment='If account is to be associated, here is where it is')
    TicketActionModDate = Column(INTEGER(10), comment='Date Of Last Modification')
    TicketActionModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User name of change to record')
    TicketActionUUID = Column(String(36), comment='Ticket Action UUID')


class Vendor(Base):
    __tablename__ = 'Vendor'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    UUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='UUID')
    Vendor = Column(String(64), nullable=False, server_default=text("'0'"), comment='Vendor Name')
    VendorComment = Column(String(256), comment='Comment about Vendor')
    Profile = Column(BIGINT(20), nullable=False, server_default=text("'0'"), comment='Profile for this type or name of module')
    ModelName = Column(String(64), nullable=False, comment='Model Name like FLASHWAVE CDS/9500/7120 etc')
    ModuleType = Column(String(64), nullable=False, server_default=text("'SYSTEM'"), comment='Module type (shelf, PSU, SFP etc)')
    ModuleName = Column(String(64), nullable=False, server_default=text("'SYSTEM'"), comment='Name of Module')
    ModDate = Column(INTEGER(10), comment='Date Of Last Modification')
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User name of change to record')


class OccrAddres(Base):
    __tablename__ = 'occr_Address'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    AddressUUID = Column(String(36), server_default=text("'0'"), comment='Address UUID')
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this address associated with')
    CustomerSiteID = Column(String(64))
    DeptProfile = Column(String(32), server_default=text("'0'"), comment='Profile or classification for this Address')
    Add_Name = Column(String(64), comment='Arbitrary label for address location')
    GPSLAT = Column(Float(asdecimal=True), server_default=text("'0'"))
    GPSLON = Column(Float(asdecimal=True), server_default=text("'0'"))
    EntryLAT = Column(Float(asdecimal=True), server_default=text("'0'"), comment='Lattitude value for gate/driveway entry point')
    EntryLON = Column(Float(asdecimal=True), server_default=text("'0'"), comment='Gate/drive entry Longitude value')
    FullAddress = Column(String(256), comment='Temp Field for Reconciling')
    Street1 = Column(String(50), server_default=text("'0'"))
    Street2 = Column(String(50), server_default=text("'0'"))
    AddSuite = Column(String(24), comment='Suite number etc')
    City = Column(String(36))
    State_Province = Column(String(36))
    PostCode = Column(String(12))
    PostCodePlus = Column(String(12))
    Country = Column(String(36))
    Building = Column(String(36), server_default=text("'0'"))
    County_Parrish = Column(String(36))
    AddressExtra = Column(String(36))
    OSMResp = Column(String(36), nullable=False, server_default=text("'FUJITSU'"), comment='OSM Responsibility - if it varies from Fujitsu ')
    AddressNote = Column(String(1024))
    Directions = Column(String(1024))
    MapURI = Column(String(256), comment='http://maps.google.com/maps?q=$latitude,$longitude')
    AccessHours = Column(String(36), server_default=text("'0000-2400'"), comment='Hours of operation or availability to access site')
    AccessDetail = Column(String(1024), comment='Details for access to address')
    AccessPerson = Column(String(36), comment='UUID of access contact')
    KeyDetail = Column(String(1024), comment='Details for keys to address')
    KeyPerson = Column(String(36), comment='UUID of access contact for keys')
    MaintDetail = Column(String(1024), comment='Details for maint svcs at address')
    MaintPerson = Column(String(36), comment='UUID of maint svcs contact')
    PowerDetail = Column(String(1024), comment='Details for power issues at address')
    PowerPerson = Column(String(36), comment='UUID of contact for power issues')
    SiteNOCDetail = Column(String(1024), comment='Details for NOC responsible for address')
    SiteNOCPerson = Column(String(36), comment='UUID of NOC contact')
    SiteWarnings = Column(String(1024), comment='Details for access to address')
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User')
    ModDate = Column(BIGINT(20), comment='Date Of Last Modification')
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='User to make  last modification')


class OccrCompany(Base):
    __tablename__ = 'occr_Company'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36))
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this company associated with')
    CustAcct = Column(String(24), comment='Customer Account Number if applicable')
    CompanyName = Column(String(64), comment='Arbitrary label for company name or display name')
    CoProfile = Column(INTEGER(16), server_default=text("'0'"), comment='No known Use')
    CompanyURL = Column(String(1024), comment='URL of company Website')
    CoAddUUID = Column(String(36), comment='UUID of Company Address')
    Note = Column(String(256))
    CreateDate = Column(BIGINT(20))
    CreateUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    ModDate = Column(BIGINT(20))
    ModUser = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class OccrContact(Base):
    __tablename__ = 'occr_Contacts'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='Record Number')
    UUID = Column(String(36))
    AcctAssoc = Column(String(24), server_default=text("'0'"), comment='What account is this address associated with')
    CustomerAccount = Column(String(36), comment="Our customer''s customer account number")
    ContactProfile = Column(String(32), server_default=text("'0'"), comment='Profile or classification ID for this contact')
    Name_Label = Column(String(64), comment='Descriptive label or name')
    FirstName = Column(String(24), server_default=text("'0'"))
    LastName = Column(String(24), server_default=text("'0'"))
    Prefix = Column(String(12), server_default=text("'0'"), comment='Mr Mrs Ms etc')
    Title = Column(String(64), server_default=text("'0'"))
    Role = Column(String(64), server_default=text("'0'"), comment='Description of persons role')
    BussAdd1 = Column(String(36), comment='UUID to 1st buss address')
    BussAdd2 = Column(String(36), comment='UUID to 2st buss address')
    DeliveryAdd = Column(String(36), comment='UUID to delivery address')
    HomeAddress = Column(String(36), comment='UUID to home address')
    BussEmail = Column(String(64), comment='business email address')
    PersEmail = Column(String(64), comment='personal email address')
    AltEmail = Column(String(64), comment='alternate email address')
    BussPhone1 = Column(String(16))
    BussExt1 = Column(String(8))
    BussPhone2 = Column(String(16))
    BussExt2 = Column(String(8))
    BussFax = Column(String(16))
    Mobile = Column(String(16))
    Pager = Column(String(16))
    Voicemail = Column(String(16))
    Admin = Column(String(36), comment='UUID of admin contact record')
    Company = Column(String(36), comment='UUID of company contact record')
    BussGroup = Column(String(64), comment='UUID of bussiness group contact')
    AltPerson = Column(String(36), comment='UUID of alternate contact')
    EscPerson = Column(String(36), comment='UUID of list of escalation contacts records')
    ContactNote = Column(String(1024))
    CreateDate = Column(BIGINT(20), comment='Epoch Date this record was added')
    CreateUser = Column(INTEGER(10), comment='User ID that created this record')
    ModDate = Column(BIGINT(20), comment='Epoch Date this record was last modified')
    ModUser = Column(INTEGER(10), comment='User ID of last user to modify this record')


class OccrDAT(Base):
    __tablename__ = 'occr_DAT'

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64))
    AID = Column(String(64))
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64))
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"), comment='Lookup Value For GPS Table')
    UUID = Column(String(36), nullable=False, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='Service Logical UUID')
    VirUUID = Column(String(36), comment='Service Virtual UUID')
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    DisplayName = Column(String(128), comment='Arbitrary Device Name Label for Display purposes')


class OccrGeneral(Base):
    __tablename__ = 'occr_General'

    UniqueID = Column(INTEGER(16), primary_key=True)
    DMPUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    CSRUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    Status = Column(String(36), comment='Circuit/CCR status pre/MTO/RFO etc')
    CustWorkOrder = Column(String(36), comment='Customer work order number')
    CSRNumber = Column(String(36), comment='CSR Record Number')
    DateRcvd = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR was submitted')
    DateCSR = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CSR was created')
    DateReview = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enters review')
    DatePreMTO = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enters Build')
    DatePreProv = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR Core PreProvisioning complete')
    DateRFO = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enters RFO - last mile complete')
    DateMTO = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enter MTO')
    DateRFS = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that circuit begins carrying traffic')
    Description = Column(String(128), comment='Description of this virtual ckt by use or name etc.')
    CreateDate = Column(INTEGER(11), nullable=False, comment='Epoch date that record was created')
    CreateUser = Column(INTEGER(10), nullable=False, comment='User id that created this record')
    ModDate = Column(INTEGER(10), nullable=False, comment='Epoch date this record was last modified')
    ModUser = Column(INTEGER(10), nullable=False, comment='User ID of last modification')


class OccrProvision(Base):
    __tablename__ = 'occr_Provision'

    UniqueID = Column(INTEGER(16), primary_key=True)
    DMPUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    CSRUUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    Status = Column(VARCHAR(36), index=True, comment='Circuit/CCR status pre/MTO/RFO etc')
    CustWorkOrder = Column(VARCHAR(36), index=True, comment='Customer work order number')
    CSRNumber = Column(VARCHAR(36), index=True, comment='CSR Record Number')
    DateRcvd = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR was submitted')
    DateCSR = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CSR was created')
    DateReview = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enters review')
    DatePreMTO = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enters Build')
    DatePreProv = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR Core PreProvisioning complete')
    DateRFO = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enters RFO - last mile complete')
    DateMTO = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that CCR enter MTO')
    DateRFS = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='Epoch date that circuit begins carrying traffic')
    Description = Column(VARCHAR(128), comment='Description of this virtual ckt by use or name etc.')
    CreateDate = Column(INTEGER(11), nullable=False, comment='Epoch date that record was created')
    CreateUser = Column(INTEGER(10), nullable=False, comment='User id that created this record')
    ModDate = Column(INTEGER(10), nullable=False, comment='Epoch date this record was last modified')
    ModUser = Column(INTEGER(10), nullable=False, comment='User ID of last modification')


class OccrSvcLog(Base):
    __tablename__ = 'occr_SvcLog'

    UniqueID = Column(INTEGER(16), primary_key=True)
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    LogCktID = Column(String(128), comment='Label value for reports etc')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    DMPPeerUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    Contact = Column(String(36), comment='Address contact UUID')
    COS = Column(INTEGER(12), comment='Class Of Service')
    ModDate = Column(BIGINT(20), comment='Date of last modification')
    ModUser = Column(INTEGER(12))
    CreateDate = Column(BIGINT(20), comment='Date record was added - set on create')
    CreateUser = Column(String(36), comment='User ID of person who added this record')


class OccrSvcVir(Base):
    __tablename__ = 'occr_SvcVir'

    UniqueID = Column(INTEGER(16), primary_key=True)
    VirUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    VirCktID = Column(String(128), comment='End User circuit reference')
    RecType = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SeqNo = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    SvcLogWorkUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    BW_Down = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Bandwidth Allocation Down - Z to A')
    BW_up = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='Bandwidth Allocation Up - A to Z')
    EndUserRef = Column(String(128), comment='End user reference for this circuit')
    SvcLogProtUUID = Column(String(36))
    COS = Column(INTEGER(12), comment='Class of Service')
    Contact = Column(String(36), comment='Owner or manager type contact')
    EndUserID = Column(String(64), comment='End User ID replaces FNC ID')
    EndUser = Column(String(36), comment='EndUser Contact record')
    Description = Column(String(128), comment='Description of this virtual ckt by use or name etc.')
    DeptID = Column(INTEGER(20))
    CreateDate = Column(INTEGER(11), nullable=False, comment='Epoch date that record was created')
    CreateUser = Column(INTEGER(10), nullable=False, comment='User id that created this record')
    ModDate = Column(INTEGER(10), nullable=False, comment='Epoch date this record was last modified')
    ModUser = Column(INTEGER(10), nullable=False, comment='User ID of last modification')


class OccrOpt(Base):
    __tablename__ = 'occr_opt'

    UniqueID = Column(INTEGER(32), primary_key=True, comment='Record Number')
    CSRUUID = Column(String(36), comment='UUID of CSR that this option belongs to')
    fieldname = Column(String(36), comment='name of field ')
    FieldValue = Column(String(2048), comment='Value for field b eing updated')
    x2 = Column(String(36), comment='spare field')
    x1 = Column(String(36), server_default=text("'0'"))
    YesNo = Column(INTEGER(1), comment='For values that use a true/false or yes/no option')


class OccrSession(Base):
    __tablename__ = 'occr_sessions'

    ID = Column(String(36), primary_key=True)
    a_session = Column(Text, nullable=False)


t_occr_users = Table(
    'occr_users', metadata,
    Column('UserName', String(64), nullable=False, index=True, server_default=text("'username'"), comment='Should match LDAP username if possible'),
    Column('Password', String(64), nullable=False, server_default=text("'password'"), comment='password'),
    Column('UserFullName', String(64), nullable=False, server_default=text("'0'"), comment="User''s Full Name"),
    Column('OCCRUserID', INTEGER(10), nullable=False, server_default=text("'0'")),
    Column('UserPriv', String(20), nullable=False, server_default=text("'ro'"), comment='ro read only, rw read write etc'),
    Column('AcctAssoc', String(20), nullable=False, server_default=text("'0'"), comment='The SAP Account this user is associated with '),
    Column('Subscriber', String(36), nullable=False, server_default=text("'0'"), comment='Subscriber this user is associated with from Subscriber table'),
    Column('ContactRec', String(36), nullable=False, server_default=text("'0'"), comment='Submitter record from Contacts table')
)


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(INTEGER(32), primary_key=True)
    a_session = Column(Text, nullable=False)


class SiebelDd(Base):
    __tablename__ = 'siebel_dd'

    UniqueId = Column(INTEGER(12), primary_key=True, comment='Just something to be unique')
    dd_type = Column(String(36), nullable=False, comment='The type of dropdown - usually name')
    dd_seq = Column(INTEGER(8), nullable=False, server_default=text("'0'"), comment='preferred display sequence (top=1)')
    dd_value = Column(String(64), nullable=False, server_default=text("'0'"), comment='The value of the choice - usually numeric')
    dd_label = Column(String(64), nullable=False, comment='What is displayed in the dd list')
    dd_description = Column(String(128), comment='Description of this choice')


class SiebelStatu(Base):
    __tablename__ = 'siebel_status'

    UniqueID = Column(INTEGER(32), primary_key=True, comment='Record Number')
    CSR = Column(String(24), index=True)
    fieldname = Column(String(24), comment='name of field ')
    FieldValue = Column(String(1024), comment='Value for field b eing updated')
    ModDate = Column(String(20), comment='Date of Record ')


class SiebelStatusTest(Base):
    __tablename__ = 'siebel_status_Test'

    UniqueID = Column(INTEGER(32), primary_key=True, comment='Record Number')
    CSR = Column(String(24))
    fieldname = Column(String(24), comment='name of field ')
    FieldValue = Column(String(2048), comment='Value for field b eing updated')
    ModDate = Column(String(20), comment='Date of Record ')


class StageHzCustSiteID(Base):
    __tablename__ = 'stage_Hz_Cust_Site_ID'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    CustomerSiteID = Column(String(64), nullable=False, index=True, server_default=text("'Unknown'"), comment='Customer Site ID')
    VirCktID = Column(String(16), nullable=False, index=True, server_default=text("'000-000-0000'"), comment='Virtual Circuit Ref')
    GPSLoc = Column(String(36), nullable=False, server_default=text("''"))
    FullAddress = Column(String(256), nullable=False, server_default=text("''"))
    AccntName = Column(String(64), nullable=False, server_default=text("''"))
    SvcCfg = Column(String(64), nullable=False, server_default=text("''"))
    Department = Column(String(36), nullable=False, server_default=text("''"))
    AccntCode = Column(String(24), nullable=False, server_default=text("'0'"))
    Add_Name = Column(String(128), nullable=False, server_default=text("''"), comment='Address Name')


class StageHzSOHCN(Base):
    __tablename__ = 'stage_Hz_SOHCN'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    Class = Column(String(64), nullable=False, server_default=text("''"), comment='?')
    FCC_Eligible = Column('FCC Eligible', String(64), nullable=False, server_default=text("''"), comment='?')
    SOHCNFacilityID = Column(String(64), nullable=False, server_default=text("''"), comment='Uncertain')
    HCP = Column(String(64), nullable=False, server_default=text("''"), comment='Customer Account Name')
    Facility = Column(String(64), nullable=False, server_default=text("''"), comment='Add_Name')
    Address = Column(String(64), nullable=False, server_default=text("''"), comment='Almost Full Address')
    Status = Column(String(64), nullable=False, server_default=text("''"), comment='Hz Status')
    BillingStart = Column(String(64), nullable=False, server_default=text("''"), comment='Hz Billing Date')
    AccountID = Column(String(64), nullable=False, server_default=text("''"), comment='Horizon Account')
    Equipment = Column(String(64), nullable=False, server_default=text("''"), comment='TID')
    PoP = Column(String(64), nullable=False, server_default=text("''"), comment='POP Name')
    Network_Fujitsu_Alcatel = Column('Network Fujitsu/Alcatel', String(64), nullable=False, server_default=text("''"), comment='Fuji or Alcatel Network')
    MonitorBy = Column(String(64), nullable=False, server_default=text("''"), comment='Who monitors the network it is on')
    CircuitID = Column(String(64), nullable=False, server_default=text("''"), comment='Circuit ID')
    DeptID = Column(String(20), server_default=text("'0'"), comment='Fujitsu Department ID')


class StageHznPriRespUpdate(Base):
    __tablename__ = 'stage_HznPriRespUpdate'

    UniqueID = Column(INTEGER(10), primary_key=True)
    AccountCode = Column(String(24), index=True)
    AccountName = Column(String(64))
    AccountType = Column(String(64))
    CustomerSiteID = Column(String(64), index=True)
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    Add_Name = Column(String(64))
    ConnectDate = Column(String(24))
    FullServiceAddress = Column(String(256))
    TaxArea = Column(String(64))
    CircuitID = Column(String(64), index=True)
    PriorityResponse = Column(String(64))
    Network = Column(String(64))
    ServiceStatus = Column(String(12))
    AddressUUID = Column(String(36), index=True)


class StageHznPriorityResponse(Base):
    __tablename__ = 'stage_HznPriorityResponse'

    UniqueID = Column(INTEGER(10), primary_key=True)
    AccountCode = Column(String(24), index=True)
    AccountName = Column(String(64))
    AccountType = Column(String(64))
    CustomerSiteID = Column(String(64), index=True)
    DeptID = Column(String(32), server_default=text("'0'"), comment='Lookup ID for Department Info')
    Add_Name = Column(String(64))
    ConnectDate = Column(String(24))
    FullServiceAddress = Column(String(256))
    TaxArea = Column(String(64))
    CircuitID = Column(String(64), index=True)
    PriorityResponse = Column(String(64))
    Network = Column(String(64))
    ServiceStatus = Column(String(12))
    AddressUUID = Column(String(36), index=True)


class StageNS1500(Base):
    __tablename__ = 'stage_NS1500'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    TID = Column(String(64), nullable=False, server_default=text("'Unknown'"), comment='TID')
    MSC = Column(String(36), comment='Address information')
    VLAN = Column(String(16), nullable=False, server_default=text("'0.0.0.0'"), comment='IP Address')


class StageE7(Base):
    __tablename__ = 'stage_e7'

    UniqueID = Column(INTEGER(10), primary_key=True)
    NETWORKNAME = Column(String(36), nullable=False, server_default=text("''"))
    REGION = Column(String(36), nullable=False, server_default=text("''"))
    IPADDRESS1 = Column(String(36), nullable=False, server_default=text("''"))
    IPADDRESS2 = Column(String(36), nullable=False, server_default=text("''"))
    NETWORKLOGINNAME = Column(String(36), nullable=False, server_default=text("''"))
    PORT = Column(String(36), nullable=False, server_default=text("''"))
    HTTPPORT = Column(String(36), nullable=False, server_default=text("''"))
    HTTPSPORT = Column(String(36), nullable=False, server_default=text("''"))
    XOFFSET = Column(String(36), nullable=False, server_default=text("''"))
    YOFFSET = Column(String(36), nullable=False, server_default=text("''"))
    WIDTH = Column(String(36), nullable=False, server_default=text("''"))
    HEIGHT = Column(String(36), nullable=False, server_default=text("''"))
    CONNECTIONSTATE = Column(String(36), nullable=False, server_default=text("''"))
    SYNCHRONIZETIME = Column(String(36), nullable=False, server_default=text("''"))
    AMPAID = Column(String(36), nullable=False, server_default=text("''"))
    AUTOCONNECT = Column(String(36), nullable=False, server_default=text("''"))
    TIMEZONE = Column(String(36), nullable=False, server_default=text("''"))
    CACHEENABLED = Column(String(36), nullable=False, server_default=text("''"))
    RADIUSENABLED = Column(String(36), nullable=False, server_default=text("''"))
    SNMPPORT = Column(String(36), nullable=False, server_default=text("''"))
    SNMPVERSIONSUPPORT = Column(String(36), nullable=False, server_default=text("''"))
    READCOMMUNITY = Column(String(36), nullable=False, server_default=text("''"))
    WRITECOMMUNITY = Column(String(36), nullable=False, server_default=text("''"))
    SNMPV3USER = Column(String(36), nullable=False, server_default=text("''"))
    SNMPV3AUTHPROTOCOL = Column(String(36), nullable=False, server_default=text("''"))
    SNMPV3AUTHPASSPHRASE = Column(String(36), nullable=False, server_default=text("''"))
    SNMPV3PRIVPROTOCOL = Column(String(36), nullable=False, server_default=text("''"))
    SNMPV3PRIVPASSPHRASE = Column(String(36), nullable=False, server_default=text("''"))
    SNMPINFORM = Column(String(36), nullable=False, server_default=text("''"))
    PROFILE = Column(String(36), nullable=False, server_default=text("''"))
    DEVICETYPE = Column(String(36), nullable=False, server_default=text("''"))
    RUNNINGVERSION = Column(String(36), nullable=False, server_default=text("''"))
    GLOBALPROFILEENABLED = Column(String(36), nullable=False, server_default=text("''"))


class StageJuniper(Base):
    __tablename__ = 'stage_juniper'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    TID = Column(String(36), nullable=False, server_default=text("'Unknown'"), comment='TID')
    Location = Column(String(256), comment='Address information')
    IPAddress = Column(String(16), nullable=False, server_default=text("'0.0.0.0'"), comment='IP Address')
    Model = Column(String(64), nullable=False, comment='Model Name like FLASHWAVE CDS/9500/7120 etc')
    SerialNum = Column(String(64), nullable=False, server_default=text("'Unknown'"), comment='serial number')
    VendorUUID = Column(String(36), nullable=False, server_default=text("'0'"), comment='UUID from Vendor table')


class StageOrion(Base):
    __tablename__ = 'stage_orion'

    UniqueID = Column(INTEGER(10), primary_key=True, comment='AutoIncrement ID value')
    NodeID = Column(INTEGER(24), nullable=False, comment='Orion Node ID - number')
    TID = Column(String(128), nullable=False, server_default=text("'Unknown'"), comment='Hostname')
    IPAddress = Column(String(24), nullable=False, server_default=text("'0.0.0.0'"), comment='IP Address')
    MachineType = Column(String(64), nullable=False, server_default=text("''"), comment='Orion Machine Type')
    InterfaceID = Column(INTEGER(24), nullable=False, comment='Orion Interface ID - number')
    Interface = Column(String(128), nullable=False, comment='Orion Interface Name')
    IfceAlias = Column(String(128), comment='Orion Interface Alias')
    Description = Column(String(256), nullable=False, server_default=text("''"))
    NotificationGroup = Column(String(64), nullable=False, server_default=text("''"))
    SubscriberName = Column(String(128), nullable=False, server_default=text("''"))
    Location = Column(String(256), nullable=False, server_default=text("''"))
    Address = Column(String(256), nullable=False, server_default=text("''"))
    City = Column(String(64), nullable=False, server_default=text("''"))
    Comments = Column(String(256), nullable=False, server_default=text("''"))
    Department = Column(String(64), nullable=False, server_default=text("''"))
