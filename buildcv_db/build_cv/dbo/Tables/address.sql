CREATE TABLE [dbo].[address] (
    [Id]         INT           NOT NULL,
    [country_id] INT           NOT NULL,
    [city]       VARCHAR (20)  NOT NULL,
    [user_id]    VARCHAR (120) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
GO


ALTER TABLE [dbo].[address]
    ADD CONSTRAINT [FK_address_user_id] FOREIGN KEY ([user_id]) REFERENCES [dbo].[users] ([uid]);
GO


ALTER TABLE [dbo].[address]
    ADD CONSTRAINT [FK_country_id_address] FOREIGN KEY ([country_id]) REFERENCES [dbo].[country] ([id]);
GO

