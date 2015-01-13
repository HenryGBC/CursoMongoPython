<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Hello World</title>
</head>
<body>
	<h1>Welcome {{username}}</h1>
<ul>
	%for thing in things:
	<li>{{thing}}</li>
	%end
</ul>
<p>
	<form action="/favorite_fruit" method="POST">
		what its your favorite fruit?
		<input type="text" name="fruit" >
		<input type="submit" value="Submit">
	</form>
</p>
</body>
</html>