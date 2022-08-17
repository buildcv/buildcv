CREATE TABLE [dbo].[degree] (
    [id]         INT          NOT NULL,
    [name]       VARCHAR (30) NULL,
    [country_id] INT          NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    FOREIGN KEY ([country_id]) REFERENCES [dbo].[country] ([id])
);
GO

