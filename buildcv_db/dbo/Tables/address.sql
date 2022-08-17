CREATE TABLE [dbo].[address] (
    [Id]      INT          NOT NULL,
    [country] VARCHAR (20) NOT NULL,
    [city]    VARCHAR (20) NOT NULL,
    [user_id] INT          NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC),
    FOREIGN KEY ([user_id]) REFERENCES [dbo].[users] ([Id])
);
GO

