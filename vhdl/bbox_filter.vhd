
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity bbox_filter is
    Port (
        clk    : in STD_LOGIC;
        conf   : in STD_LOGIC_VECTOR(15 downto 0);
        enable : in STD_LOGIC;
        keep   : out STD_LOGIC
    );
end bbox_filter;

architecture Behavioral of bbox_filter is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if enable = '1' then
                if to_integer(unsigned(conf)) > 32767 then
                    keep <= '1';
                else
                    keep <= '0';
                end if;
            end if;
        end if;
    end process;
end Behavioral;
