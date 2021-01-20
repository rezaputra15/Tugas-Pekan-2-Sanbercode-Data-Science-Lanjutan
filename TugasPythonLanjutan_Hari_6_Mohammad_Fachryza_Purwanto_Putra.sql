SELECT a.Title, b.Name, c.Name AS Track 
FROM albums a 
INNER JOIN artists b 
    ON
    a.ArtistId = b.ArtistId
LEFT JOIN tracks c
    ON 
    a.AlbumId = c.AlbumId
WHERE b.Name == 'AC/DC' AND a.Title == 'Let There Be Rock' OR b.Name == 'Aerosmith';