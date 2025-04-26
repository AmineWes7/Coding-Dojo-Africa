import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpSession;
import javax.validation.Valid;

@Controller
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/register")
    public String showRegistrationForm(Model model) {
        model.addAttribute("user", new User());
        return "register";
    }

    @PostMapping("/register")
    public String registerUser(@Valid @ModelAttribute("user") User user, BindingResult result, Model model) {
        if (result.hasErrors()) {
            return "register";
        }
        userService.registerUser(user);
        return "redirect:/login";
    }

    @GetMapping("/login")
    public String showLoginForm(Model model) {
        model.addAttribute("loginUser", new LoginUser());
        return "login";
    }

    @PostMapping("/login")
    public String loginUser(@Valid @ModelAttribute("loginUser") LoginUser loginUser, BindingResult result, HttpSession session) {
        if (result.hasErrors()) {
            return "login";
        }
        Optional<User> userOpt = userService.authenticateUser(loginUser.getEmail(), loginUser.getPassword());
        if (userOpt.isPresent()) {
            session.setAttribute("userId", userOpt.get().getId());
            return "redirect:/success";
 }
        result.rejectValue("email", "error.loginUser ", "Invalid email or password");
        return "login";
    }

    @GetMapping("/success")
    public String successPage(HttpSession session) {
        if (session.getAttribute("userId") == null) {
            return "redirect:/login";
        }
        return "success";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/login";
    }
}