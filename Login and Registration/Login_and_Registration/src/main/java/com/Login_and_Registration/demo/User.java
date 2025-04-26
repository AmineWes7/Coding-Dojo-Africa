import javax.persistence.*;
import javax.validation.constraints.*;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "Username is required")
    @Pattern(regexp = "^[a-zA-Z]{3,}$", message = "Username must be at least 3 letters")
    private String username;

    @NotBlank(message = "Email is required")
    @Email(message = "Email should be valid")
    @Column(unique = true)
    private String email;

    @NotBlank(message = "Password is required")
    @Size(min = 8, message = "Password must be at least 8 characters")
    @Pattern(regexp = "^(?=.*[A-Z])(?=.*\\d).+$", message = "Password must contain at least one uppercase letter and one number")
    private String password;

    @Transient
    @NotBlank(message = "Password confirmation is required")
    private String passwordConfirmation;

    // Getters and Setters

    public void setPassword(String password) {
        this.password = new BCryptPasswordEncoder().encode(password);
    }
}