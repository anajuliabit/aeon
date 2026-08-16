/^---$/ { n++; next }
n == 1 { print FILENAME ": " $0 }
/^depends_on:|^- skill:|consume:|parallel:|trigger:/ { print $0 }
