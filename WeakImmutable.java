

import java.util.Date;

public final class WeakImmutable {
    private final String name; //immutable
    private final Date birthDate; //mutable

    public WeakImmutable(String name, Date birthDate) {
        this.name = name;
        this.birthDate = new Date(birthDate.getTime()); // Defensive copy
    }

    public String getName() {
        return name;
    }

    public Date getBirthDate() {
        return new Date(birthDate.getTime()); // Return a defensive copy
    }
}
