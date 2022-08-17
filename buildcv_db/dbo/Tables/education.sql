CREATE TABLE [dbo].[education] (
    [id]         INT          NOT NULL,
    [university] VARCHAR (30) NULL,
    [degreee]    INT          NULL,
    [country_id] INT          NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    FOREIGN KEY ([country_id]) REFERENCES [dbo].[country] ([id])
);
GO

