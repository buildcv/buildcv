CREATE TABLE [dbo].[users] (
    [name]     VARCHAR (60)  NOT NULL,
    [birthday] DATE          NOT NULL,
    [uid]      VARCHAR (100) NOT NULL,
    [email]    VARCHAR (30)  NOT NULL,
    [id]       INT           IDENTITY (1, 1) NOT NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);
GO

