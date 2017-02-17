<?php 
$dir = '.';
$files = scandir($dir, 0);
?>
<ul>
<?php for($i = 2; $i < count($files); $i++)
    echo '<li><a href = "' .$files[$i]. '" > ' .$files[$i]. ' </a></li>';
?>
</ul>

