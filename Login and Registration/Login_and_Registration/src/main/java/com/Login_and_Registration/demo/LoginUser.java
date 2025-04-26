import javax.validation.constraints.*;

public class LoginUser {
    @NotBlank(message = "Email is required")
    private String email;

    @NotBlank(message = "Password is required")
    private String password;

    // Getters and Setters
}