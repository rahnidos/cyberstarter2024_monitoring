param(
  
 [Parameter(Mandatory=$true)][Int]$days,
 [Parameter(Mandatory=$true)][String]$size,
 [String]$filter = "*.*"
)
$folder='C:\em_file'
$now=Get-Date
$okdate=$now.AddDays(-$days)
$files=Get-ChildItem -recurse $folder -include $filter -file | Where {$_.LastWriteTime -ge "$okdate"}
foreach ($file in $files)
{
   if ($file.Length -lt $size
   ) {
    echo "WARNING: File seems to be quite small, better check it!"
    exit 1
   }
   else {
    echo "OK"
    exit 0
   }
}
echo "CRITICAL: There is no fresh backup file"
exit 2