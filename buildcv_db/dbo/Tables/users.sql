CREATE TABLE [dbo].[users] (
    [Id]       INT           NOT NULL,
    [name]     VARCHAR (60)  NOT NULL,
    [birthday] DATE          NOT NULL,
    [uid]      VARCHAR (100) NOT NULL,
    [email]    VARCHAR (30)  NOT NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
GO

