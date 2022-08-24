CREATE TABLE [dbo].[usercvs] (
    [Id]            INT           IDENTITY (1, 1) NOT NULL,
    [cv_table_name] VARCHAR (120) NOT NULL,
    [user_uid]      VARCHAR (120) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC),
    FOREIGN KEY ([user_uid]) REFERENCES [dbo].[users] ([uid])
);
