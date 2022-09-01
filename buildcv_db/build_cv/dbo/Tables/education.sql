CREATE TABLE [dbo].[education] (
    [id]         INT           NOT NULL,
    [university] VARCHAR (30)  NULL,
    [degreee]    INT           NULL,
    [country_id] INT           NULL,
    [user_id]    VARCHAR (120) NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    FOREIGN KEY ([country_id]) REFERENCES [dbo].[country] ([id])
);
GO


ALTER TABLE [dbo].[education]
    ADD CONSTRAINT [FK_education_user_id] FOREIGN KEY ([user_id]) REFERENCES [dbo].[users] ([uid]);
GO

