Expression:
density

Code Block:
Dim density
If [POP90_SQMI] < 100 Then
density = "low"

ElseIf [POP90_SQMI] < 300 Then
density = "medium"

Else
density = "high"
End If